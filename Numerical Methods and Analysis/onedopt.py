"""
One Dimensional Optimizer written in Python
by: Jose Aries E. De Los Santos
"""
import numpy as np
import matplotlib as mpl
mpl.use("qt4agg")
import matplotlib.pyplot as plt

#Define the function

def f(x):
    return (x-1)**4 + 8

def f1(f,x,h):
    """
    Finite Difference Method for the First Derivative, Three-point Formula
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def f2(f,x,h):
    """
    Finite Difference Method for the Second Derivative, Three-point Formula
    """
    return (f(x - h) - 2 * f(x) + f(x + h)) / (h**2)

#Initialization
x0 = -10; tol = 1e-7; h = 1e-4; max_iter = 2e+3

#Optimizer Algorithm
x = x0
iter = 0
xdict = []
while iter < max_iter:
    xdict.append(x)
    y1 = f1(f,x,h)
    y2 = f2(f,x,h)
    if np.abs(y1) < tol and y2 > 0:
        break
    else:
        t = - (y1/y2)
        x = x + t
        iter = iter + 1


#Post Processing
xoutput = x

print("Optimal solution:", xoutput)
print("Number of Iterations:",iter)

#Plotting

xdict = np.array(xdict)
ydict = []
for i in range(np.size(xdict)):
    y = f(xdict[i])
    ydict.append(y)
ydict = np.array(ydict)

v = np.linspace(-10,10,100)
fig, ax = plt.subplots(figsize=(12,4))
plt.style.use("seaborn-poster")
ax.set_title("One Dimension Optimizer for\n" + r"$f(x) = (x-1)^4+8$",fontsize=14)
ax.plot(v,f(v),"k-",lw=1.5); ax.plot(xdict[0],f(xdict[0]),marker="*",markersize=10,color="#000033",label="Starting Point")
for i in range(1,np.size(xdict)):
    ax.plot(xdict[i],f(xdict[i]),marker="v",markersize=6,color="#00b200")
ax.plot(xdict,ydict,"m--",lw=1)
ax.annotate("Starting point",fontsize=14,family="serif",
            xy=(xdict[0],f(xdict[0])),xycoords="data",
            xytext=(+95,-30),textcoords="offset points",
            arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3, rad=-0.5"))
ax.plot(xoutput,f(xoutput),marker="*",markersize=15,color="#aa0000",label="Optimal Solution")
ax.annotate("Optimal Solution approximately at %.5f" % xoutput,fontsize=14,family="serif",
            xy=(xoutput,f(xoutput)),xycoords="data",
            xytext=(-150,+50), textcoords="offset points",
            arrowprops=dict(arrowstyle="-|>",connectionstyle="arc3, rad=-0.5"))
ax.legend(loc=1,fontsize=14)
plt.show()