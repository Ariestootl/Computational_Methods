#Bessel Functions
#Plotting using Simpson's Rule
#by Jose Aries E. De Los Santos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Initialization
n = 100
a = 0; b = np.pi; h = (b-a)/n 
t = np.arange(a,b,h); x = np.linspace(0,20,n)



def simpson(f,a,b,t,h):
    """
    Calculate Integration using Simpson's Rule
    """
    return h*(f(a)+2*np.sum(f(t[2::2]))+4*np.sum(f(t[1::2]))+f(b))/3

#Creating Bessel Functions

#for n=0
j0 = []
for i in x:
    f0 = lambda t: np.cos(i*np.sin(t)-0*t)
    j0store = simpson(f0,a,b,t,h)
    j0.append(j0store)
#for n=1
j1 = []
for i in x:
    f0 = lambda t: np.cos(i*np.sin(t)-1*t)
    j1store = simpson(f0,a,b,t,h)
    j1.append(j1store)
#for n=2
j2 = []
for i in x:
    f0 = lambda t: np.cos(i*np.sin(t)-2*t)
    j2store = simpson(f0,a,b,t,h)
    j2.append(j2store)

j0 = np.array([j0])
j1 = np.array([j1])
j2 = np.array([j2])

#Plotting
fig, ax = plt.subplots(figsize=(12,7))
ax.plot(x,j0.flatten(),"b-",label=r"$J_0(x) = \frac{1}{\pi} \int_{0}^{\pi} \cos(x\sin(\theta)-0\theta)$")
ax.plot(x,j1.flatten(),"r-",label=r"$J_1(x) = \frac{1}{\pi} \int_{0}^{\pi} \cos(x\sin(\theta)-\theta)$")
ax.plot(x,j2.flatten(),"m-",label=r"$J_2(x) = \frac{1}{\pi} \int_{0}^{\pi} \cos(x\sin(\theta)-2\theta)$")
ax.set_title("Graph of Bessel Functions for n = 0,1,2 of:  " + r"$J_n(x) = \frac{1}{\pi} \int_{0}^{\pi} \cos(x\sin(\theta)-n\theta)$" + "\n Approximate Integration via Simpson's Rule",fontsize=14)
ax.set_xlabel(r"$x$",fontsize=14)
ax.set_ylabel(r"$y$",fontsize=14)
ax.legend(loc=1,fontsize=14)
plt.grid(True)
plt.show()