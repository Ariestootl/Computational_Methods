#Predator-Prey Model
#by: Jose Aries E. De Los Santos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

N=1000; a=0;b=30;h=(b-a)/N; t = np.arange(a,b,h)
def f(t,y):
    return np.array([-0.16*y[0]+0.08*y[0]*y[1],4.5*y[1]-0.9*y[0]*y[1]])

def rk4(t, y, h):
    """
    Explicit Runge-Kutta Order 4 Method
    """
    s1 = f(t, y)
    s2 = f(t + h/2, y + s1 * (h/2))
    s3 = f(t + h/2, y + s2 * (h/2))
    s4 = f(t + h, y + h * s3)
    return y + h * (s1 + 2*s2 + 2*s3 + s4) / 6

y1 = np.zeros((2, N))
y1[:, 0] = np.array([4,4])

for i in range(N - 1):
    y1[:, i + 1] = y1[:, i] + h * f(t[i], y1[:, i])

y5 = np.zeros((2, N))
y5[:, 0] = np.array([4,4])

for i in range(N - 1):
    y5[:, i + 1] = rk4(t[i], y5[:, i], h)

fig, ax = plt.subplots(figsize=(16,4))
plt.style.use("seaborn-poster")
ax.plot(t,y5[0,:],ls="-.",lw=1.5,color="#0000FF",label="Predator")
ax.plot(t,y5[1,:],ls="--",lw=1.5,color="#FF0000",label="Prey")
ax.plot(t,y1[0,:],ls="-.",lw=1.5,color="#0000aa",label="Predator")
ax.plot(t,y1[1,:],ls="--",lw=1.5,color="#aa0000",label="Prey")
ax.set_xlabel("Time",fontsize=13)
ax.set_ylabel("Population",fontsize=13)
ax.set_title("An Example of Lotka-Volterra Predator-Prey Model \n Explicit Runge-Kutta Order 4 v.s. Forward Euler",fontsize=13)
ax.legend(bbox_to_anchor=(1.01,1), loc=2, borderaxespad=0.0,ncol=1)
fig.subplots_adjust(right=0.85)
plt.show()