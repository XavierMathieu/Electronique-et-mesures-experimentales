#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

Données = []

for i in range(15):
    a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 5/Labo 5 mesures/Labo 5 Partie 1 resistance avec condensateurs {i+1}.lvm')
    data = a[0]["data"]
    
    R = np.mean(data[:, 0])
    I_R = np.std(data[:, 0])/math.sqrt(30)
    
    V = np.mean(data[:, 1]*1000)
    I_V = np.std(data[:, 1]*1000)/math.sqrt(30)
    
    Données += [[R, I_R, V, I_V]]

Données = np.array(Données)

Res = np.sort(Données[:, 0])
I_Res = np.sort(Données[:, 1])
Ten = np.sort(Données[:, 2])
I_Ten = np.sort(Données[:, 3])

#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)


plt.errorbar(Res, Ten, xerr = I_Res, yerr = I_Ten, mfc = "black", ms = 4, ls = "-")
plt.xlabel("Résistance (Ohm)")
plt.ylabel("Tension efficace (mV)")

caption = """
Figure 2:  
"""

plt.text(0.07, 0.2, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 3/Graphique I-V bobine.pdf")








# %%
