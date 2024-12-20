#To display some basic line properties in matplotlib

import numpy as np
import sympy
sympy.init_printing()
import matplotlib as mpl
mpl.use("qt4agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.linspace(-5,5,5)
y = np.ones_like(x)

def axes_settings(fig,ax,title,ymax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0,ymax+1)
    ax.set_title(title)

fig, axes = plt.subplots(nrows=1,ncols=4,figsize=(16,4))

#Line width

linewidths = [0.5,1.0,2.0,4.0]
for n, linewidth in enumerate(linewidths):
    axes[0].plot(x,y+n,color="blue",linewidth=linewidth)
axes_settings(fig,axes[0],"linewidth",len(linewidths))

#Line Style
linestyles = ["-","-.",":"]
for n, linestyle in enumerate(linestyles):
    axes[1].plot(x,y+n,color="blue",lw=2,linestyle=linestyle)

#custom dash style
line, = axes[1].plot(x,y+3,color="blue",lw=2)
length1,gap1,length2,gap2 = 10,7,20,7
line.set_dashes([length1,gap1,length2,gap2])
axes_settings(fig,axes[1],"linetpyes",len(linestyles)+1)

#marker types
markers = ['+', 'o','*','s','.','1','2','3','4']
for n, marker in enumerate(markers):
    axes[2].plot(x,y+n,color="blue",lw=2,ls='None',marker=marker)
axes_settings(fig,axes[2],"markers",len(markers))

#marker size
markersizecolors = [(4,"white"),(8,"red"),(12,"yellow"),(16,"lightgreen")]
for n,(markersize, markerfacecolor) in enumerate(markersizecolors):
    axes[3].plot(x,y+n,color="blue",lw=1,ls="-",marker='o',markersize=markersize,markerfacecolor=markerfacecolor,markeredgewidth=2)
axes_settings(fig,axes[3],"marker size/color",len(markersizecolors))
plt.show()
