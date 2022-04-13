#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math



#%%
R = [180000, 13500, 7660, 5460, 3050, 2390, 1830, 1330, 944, 781, 669, 599, 564, 524, 506] 
RPM = [192, 230, 236, 285, 311, 344, 365, 397, 429, 463, 474, 484, 502, 502, 502]


#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
#fig.subplots_adjust(bottom=0.3)
plt.xscale("log")
plt.plot(R, RPM, ls = '-', ms = 0, label="RMP")
#plt.plot(np.linspace(0, 10000000, 1000), (max(20*np.log10(G_w(W)))-3)*np.ones(1000), color="green", ms = 0, ls = "-")
plt.xlabel("Résistance [Ohm]")
plt.ylabel("Rotations par minute [RPM]")
plt.legend()
#plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Conception RPM echelle log.pdf")
# %%
