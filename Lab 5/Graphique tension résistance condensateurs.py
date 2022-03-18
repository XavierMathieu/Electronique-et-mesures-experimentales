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
    
    V = np.mean(data[:, 1])
    I_V = np.std(data[:, 1])/math.sqrt(30)

    P = (V**2)/R
    I_P = math.sqrt(2*(I_V/V)**2 + (I_R/R)**2)*P

    mesure = [R, I_R, P, I_P]

    Ajout = True

    for j in Données:
        if j[0] > R:
            Données.insert(Données.index(j), mesure)
            Ajout = False
            break
    if Ajout:
        Données += [mesure]

Données = np.array(Données)

Res = (Données[:, 0])
I_Res = (Données[:, 1])
Ten = (Données[:, 2])
I_Ten = (Données[:, 3])

#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

plt.xscale("log")
plt.errorbar(Res, Ten, xerr = I_Res, yerr = I_Ten, mfc = "black", ms = 4, ls = "-")
plt.xlabel("Résistance (Ohm)")
plt.ylabel("Tension efficace (mV)")

caption = """
Figure 2: Puissance en
fonction de la résistance totale du circuit (Ohm)
dans la circuit sans condensateurs en parallèle
"""

plt.text(0.07, 0.2, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 5/Graphique tension efficace condensateur.pdf")








# %%
