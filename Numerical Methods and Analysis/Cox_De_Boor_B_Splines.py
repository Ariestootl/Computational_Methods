import numpy as np
import torch
import matplotlib.pyplot as plt

def b_splines(x: torch.Tensor, grid: torch.Tensor, spline_order: int):  ### Cox-De Boor Recursion
    """
    Compute the B-spline bases for the given input tensor.

    Args:
        x (torch.Tensor): Input tensor of shape (batch_size, in_features).

    Returns:
        torch.Tensor: B-spline bases tensor of shape (batch_size, in_features, grid_size + spline_order).
    """
    x = x.unsqueeze(-1)
    bases = ((x >= grid[:, :-1]) & (x < grid[:, 1:])).to(x.dtype)


    ## Cox and De Boor Recursion Algorithm for B Splines

    # Compute higher-order B-spline bases recursively
    for k in range(1, spline_order + 1):
        bases = (
            (x - grid[:, : -(k + 1)])
            / (grid[:, k:-1] - grid[:, : -(k + 1)])
            * bases[:, :, :-1]  # B_{i,k-1}(x) left term
        ) + (
            (grid[:, k + 1 :] - x)
            / (grid[:, k + 1 :] - grid[:, 1:(-k)])
            * bases[:, :, 1:]   # B_{i+1,k-1}(x) right term
        )

    return bases.contiguous()

# Define parameters
in_features = 1
grid_size = 5
spline_order = 4
grid_range = [-1, 1]

# Compute grid
h = (grid_range[1] - grid_range[0]) / grid_size
grid = (torch.arange(-spline_order, grid_size + spline_order + 1) * h + grid_range[0]).expand(in_features, -1)

# Generate input values for plotting
x_values = torch.linspace(grid_range[0], grid_range[1], 100).unsqueeze(1)  # Shape (100, 1)

# Compute and plot basis functions
basis_functions = b_splines(x_values, grid, spline_order).numpy()

basis_functions = basis_functions.squeeze(1)  # Ensure shape is (100, 8)

plt.figure(figsize=(8, 6))
for i in range(basis_functions.shape[1]):  # Now it's (100, 8), so loop over 8
    plt.plot(x_values.numpy().flatten(), basis_functions[:, i], label=f"B_{i},{spline_order}")

plt.xlabel("x")
plt.ylabel("B-spline Basis Functions")
plt.title(f"B-spline Basis Functions (Order {spline_order})")
# plt.legend()
plt.grid()
plt.show()


