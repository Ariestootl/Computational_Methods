"""
Bisection Method in Python 
by
Jose Aries De Los Santos
"""

from scipy import linalg as la 
from scipy import optimize
import numpy as np
import sympy
sympy.init_printing()
import matplotlib as mpl
mpl.use("qt4agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

f = lambda x: np.exp(x)-2; tol = 0.1; a,b = -2,2; x = np.linspace(-2.1,2.1,1000)

fig,ax = plt.subplots(1,1,figsize=(16,7))
ax.set_title(r"Bisection Method for the function $f(x) = e^x-2$", fontsize=12)
ax.set_xlabel(r"$x$", fontsize=13); ax.set_ylabel(r"$y$", fontsize=13)
ax.plot(x,f(x),'b',lw=1.5)
ax.axhline(0,ls=':',color='k')
ax.axvline(0,ls=':',color='k')
ax.set_xticks([-2,-1,0,1,2])

# Finding the root using Bisection Method and Visualize
fa, fb = f(a),f(b); ax.plot(a,fa,"ko"); ax.plot(b,fb,"ko")
ax.text(a,fa+0.5,r"$a$", ha='center',fontsize=18); ax.text(b,fb+0.5,r"$b$",ha='center',fontsize=18)

#Bisection Method Algorithm
iter=1
while b-a > tol:
    m = a + (b-a)/2
    fm = f(m)

    ax.plot(m,fm,"ko")
    ax.text(m,fm-0.5,r"$m_%d$" % iter, ha="center")
    iter = iter+1

    if np.sign(fa) == np.sign(fm):
        a,fa = m,fm
    else:
        b,fb = m,fm
ax.plot(m,fm,"r*",markersize=12)
ax.annotate("Root approximately at %.5f" % m, xy = (a,fm),xycoords='data',xytext=(-150,+50), textcoords = "offset points",
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3, rad=-.5"),fontsize=14,family="serif")
plt.show()