# Testing our Numerical Methods in Python 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sympy
sympy.init_printing()

# plt.style.use("seaborn-colorblind")
# plt.figure(figsize = (10,7))
# x = np.linspace(-5,5,30)
# plt.title(f"Plotting various Polynomials from {x[0]} to {x[-1]}", fontsize=18)
# plt.plot(x,x**2,"r*", label = "Quadratic")
# plt.plot(x,x**3,"ko", label = "Cubic")

# plt.xlabel("X-axis", fontsize=18)
# plt.ylabel("Y-axis", fontsize=18)
# plt.legend(loc=2,fontsize=18)
# plt.xlim(-6,6)
# plt.ylim(-10,10)
# plt.grid()


## Different types of Plots
# x = np.arange(11) 
# y = x**2

# plt.figure(figsize = (14,8))

# plt.subplot(2,3,1)
# plt.title("Plot")
# plt.plot(x,y,"b")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid

# plt.subplot(2,3,2)
# plt.title("Scatter")
# plt.scatter(x,y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid

# plt.subplot(2,3,3)
# plt.title("Semilogy")
# plt.semilogy(x,y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid

# plt.subplot(2,3,4)
# plt.title("Semilogx")
# plt.semilogx(x,y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid

# plt.subplot(2,3,5)
# plt.title("Loglog")
# plt.loglog(x,y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid

# plt.subplot(2,3,6)
# plt.title("Bar")
# plt.bar(x,y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid

# plt.tight_layout()


#Surface Plot

fig = plt.figure(figsize=(12,10))
ax = plt.axes(projection="3d")

x = np.arange(-5, 5.1, 0.2)
y = np.arange(-5,5.1,0.2)
X,Y = np.meshgrid(x,y)
Z = np.sin(X)*np.cos(Y)

surf  = ax.plot_surface(X,Y,Z,cmap = plt.cm.cividis)
ax.set_title("Surface Plot")
ax.set_xlabel("x", labelpad=20)
ax.set_ylabel("y", labelpad=20)
ax.set_zlabel("z", labelpad=20)

fig.colorbar(surf, shrink=0.5, aspect=8)

plt.show()