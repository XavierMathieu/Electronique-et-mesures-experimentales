#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Alu-Zinc_1V_28_01_2022.lvm')
Tension = a[0]["data"]*1000
n_bins = 20
dist1 = Tension

fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

plt.hist(dist1, bins=n_bins, edgecolor='black', facecolor="lightgrey")
plt.minorticks_on()
plt.xlabel("Tension mesurée (mV)")
plt.ylabel("Nombre de données")

caption = """
Figure 4: Distribution des valeurs de tensions aux bornes d'une patate 
avec un couple d'électrodes aluminium-zinc en circuit ouvert (i.e. aucune 
résistance de charge, seulement le voltmètre) à une résolution de ±1V.
"""

plt.text(0, 0.20, caption, fontsize='large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 1/Patate_Alu-Zinc_1V.pdf")
# %%
