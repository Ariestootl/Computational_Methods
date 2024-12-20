"""
Newton's Method Numerical Analysis performed using Python
by: Jose Aries E. De Los Santos
"""

from scipy import linalg as la 
from scipy import optimize
import numpy as np
import sympy
sympy.init_printing()
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# define a function, desired tolerance, and starting point
tol = 0.001; xk = 2; s_x = sympy.symbols("x"); s_f = sympy.exp(s_x) - 2

f = lambda x: sympy.lambdify(s_x,s_f,'numpy')(x)
fd = lambda x: sympy.lambdify(s_x,sympy.diff(s_f,s_x),'numpy')(x)

x = np.linspace(-1,2.1,1000)

#setup the graph for visualizing the root finding steps
fig, ax = plt.subplots(1,1,figsize=(16,7))
ax.set_title(r"Newton's Method for $f(x) = e^x - 2$", fontsize=18)
ax.plot(x,f(x),"#0000aa",ls="-",lw=2)
ax.axhline(0,ls="-.",color='k',lw=1)
ax.axvline(0,ls="-.",color='k',lw=1)
ax.grid(color="#000000",lw=0.5,ls=":")

#iterate Newton's Method until convergence to the desired tolerance is achieved

iter = 0
while f(xk) > tol:
    xk_new = xk - (f(xk)/fd(xk))

    ax.plot([xk,xk],[0,f(xk)],color='k',ls=":")
    ax.plot(xk,f(xk),'mo')
    ax.text(xk,-0.5,r"$x_%d$" % iter,ha="center")
    ax.plot([xk,xk_new],[f(xk),0],"k-")

    xk = xk_new
    iter = iter + 1

ax.plot(xk,f(xk), "r*", markersize=15)
ax.annotate("Root approximately at %.8f" % xk, fontsize=14,family="serif",
            xy=(xk,f(xk)),xycoords="data",
            xytext=(-150,+50), textcoords="offset points",
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3, rad=-0.5"))
ax.set_xticks([-1,0,1,2])
plt.show()
