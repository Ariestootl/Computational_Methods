import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



#3D Plot of Helix

# fig = plt.figure(figsize=(10,10))
# ax = plt.axes(projection="3d")
# ax.grid()
# t = np.arange(10, 10*np.pi, np.pi/50)

# x = np.sin(t)
# y = np.cos(t)

# ax.plot3D(x,y,t)
# ax.set_title("3D Parametric Plot")
# ax.set_xlabel("x", labelpad=20)
# ax.set_ylabel("y", labelpad=20)
# ax.set_zlabel("z", labelpad=20)

#Scatter Plot

# x = np.random.random(50)
# y = np.random.random(50)
# z = np.random.random(50)

# fig = plt.figure(figsize=(10,10))
# ax = plt.axes(projection="3d")
# ax.grid()

# ax.scatter(x,y,z,c="r",s=50)

# ax.set_title("Scatter Plot")
# ax.set_xlabel("x", labelpad=20)
# ax.set_ylabel("y", labelpad=20)
# ax.set_zlabel("z", labelpad=20)


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

fig.colorbar(surf, shrink=0.5, aspect=9)

plt.show()