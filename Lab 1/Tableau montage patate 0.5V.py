#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Montage_0.5V_28_01_2022.lvm')
Tensions = a[0]["data"]*1000
patate = Tensions[:, 0]
courant = Tensions[:, 1]/12
n_bins = 20

fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

plt.hist(patate, bins=n_bins, edgecolor='black', facecolor="lightgrey")
plt.minorticks_on()
plt.xlabel("Tension mesurée (mV)")
plt.ylabel("Nombre de données")

caption = """
Figure 10: Distribution des valeurs de tensions aux bornes 
d'une patate avec un couple d'électrodes Inox-zinc en série 
avec une résistance de 1kOhm et une résistance de 12 Ohm 
(nommées dans le sens du courant) à une résolution de ±0.5V.
"""

plt.text(0.08, 0.20, caption, fontsize='large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 1/Patate_Montage_Tension_0.5V.pdf")
# %%

fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

plt.hist(courant, bins=n_bins, edgecolor='black', facecolor="lightgrey")
plt.minorticks_on()
plt.xlabel("Courant mesuré (mA)")
plt.ylabel("Nombre de données")

caption = """
Figure 11: Distribution des valeurs d'intensité du courant calculée 
avec la tension aux bornes de la résistance de 12 Ohm dans le circuit
de la patate de la figure 10 à une résolution de ±0.5V.
"""

plt.text(0, 0.20, caption, fontsize='large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 1/Patate_Montage_Courant_0.5V.pdf")
# %%
