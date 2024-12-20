from scipy import linalg as la 
from scipy import optimize
import numpy as np
import sympy
import matplotlib as mpl
mpl.use("qt4agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

sym_x = sympy.Symbol("x")
x = np.linspace(-2*np.pi,2*np.pi,100)

def sin_expansion(x,n):
    return sympy.lambdify(sym_x,sympy.sin(sym_x).series(n=n+1).removeO(), 'numpy')(x)

fig, ax = plt.subplots(figsize=(14,8))
plt.style.use("seaborn-poster")
ax.plot(x,np.sin(x),linewidth=4,color='red',label='$sin(x)$')
colors = ["blue","black"]
linestyles = [":","-.","--"]
for idx, n in enumerate(range(1,12,2)):
    ax.plot(x,sin_expansion(x,n), color=colors[idx // 3], linestyle=linestyles[idx % 3], linewidth=3, label="$order$ $%d$ $approx.$" % (n+1))

ax.set_ylim(-2,2)
ax.set_xlim(-0.5*np.pi,2.0*np.pi)
ax.set_xlabel("$x$",fontsize=18)
ax.set_ylabel("$y$",fontsize=18)
ax.set_title("Plotting Taylor Series Expansions for the function sin(x)", fontsize="18", fontname="serif", color="#003300")
ax.legend(bbox_to_anchor=(1.1,1), loc=2, borderaxespad=0.0,ncol=1)
fig.subplots_adjust(right=0.75)
plt.show()