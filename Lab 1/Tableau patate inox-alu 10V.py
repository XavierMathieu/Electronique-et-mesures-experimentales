#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Alu-inox_10V_28_01_2022.lvm')
Tension = a[0]["data"]*1000
print(len(Tension))
x = range(510)
dist1 = Tension

plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
plt.subplots_adjust(bottom=0.3)

plt.scatter(x, dist1, color="k", s=4)
plt.minorticks_on()
plt.xlabel("Tension mesurée (mV)")
plt.ylabel("Nombre de données")

caption = """
Figure 2: Distribution des valeurs de tensions aux bornes d'une patate 
avec un couple d'électrodes inox-aluminium en circuit ouvert (i.e. aucune 
résistance de charge, seulement le voltmètre) à une résolution de ±1V.
"""

plt.text(0, 0.20, caption, fontsize='large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 1/Patate_Alu-Inox_10V.pdf")
# %%
