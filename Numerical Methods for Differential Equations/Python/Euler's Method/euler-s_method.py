import numpy as np
import matplotlib.pyplot as plt

##Define the following functions
def f(t, y):
    return y + t

def forward_euler(y0, h, N, t, f):
    y = np.zeros(N)
    y[0] = y0
    for i in range(0, N-1):
        y[i+1] = y[i] + h*f(t[i], y[i])
    return y

def backward_euler(y0, h, N, t, f):
    y = np.zeros(N)
    y[0] = y0
    for i in range(0, N-1):
        y[i+1] = (y[i] + h*t[i+1]) / (1 - h);
    return y

##Set up the problem
a=0; b=5; N=100; t = np.linspace(a,b,N); 
ftrue = lambda t: (-t-1)+ np.exp(t); ###True Solution
h = (t[1]-t[0]) ;  y0 = 0;

y1 = forward_euler(y0, h, N, t, f);
y2 = backward_euler(y0, h, N, t, f);


plt.figure(figsize=(10, 6))
plt.plot(t, ftrue(t), linestyle="-", linewidth=2.0, label="True solution")
plt.plot(t, y1, linestyle="-", linewidth=2.0, color="#770000", label="Forward Euler")
plt.plot(t, y2, linestyle="-", linewidth=2.0, color="#005500", label="Backward Euler")
plt.legend(loc="upper left", fontsize=16)
plt.xlabel("t", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.show()