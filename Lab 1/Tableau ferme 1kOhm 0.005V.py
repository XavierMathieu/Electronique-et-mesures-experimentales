#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Fermé-1kOhm_0.005V_28_01_2022.lvm')
Tension = a[0]["data"]*1000
n_bins = 40
dist1 = Tension

fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

plt.hist(dist1, bins=n_bins, edgecolor='black', facecolor="lightgrey")
plt.minorticks_on()
plt.xlabel("Tension mesurée (mV)")
plt.ylabel("Nombre de données")

caption = """
Figure 9: Distribution des valeurs de tensions captées par 
le module d'aquisition sur une résistance sans alimentation 
(i.e. seulement la résistance) à une résolution de ±0,005V.
"""

plt.text(0.1, 0.20, caption, fontsize='large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 1/Circuit_fermé_1kOhm_0.005V.pdf")
# %%
