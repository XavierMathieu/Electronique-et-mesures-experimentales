#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Montage_0.5V_28_01_2022.lvm')
Tensions = a[0]["data"]*1000
patate = Tensions[:, 0]
courant = Tensions[:, 1]/12
n_bins = 20

plt.hist(patate, bins=n_bins, color="k")
plt.minorticks_on()
plt.xlabel("Tension mesurée (mV)")
plt.ylabel("Nombre de données")
plt.show
plt.savefig("Patate_Montage_Tension_0.5V", format="pdf")
# %%
plt.hist(courant, bins=n_bins, color="k")
plt.minorticks_on()
plt.xlabel("Courant mesuré (mA)")
plt.ylabel("Nombre de données")
plt.show
plt.savefig("Patate_Montage_Courant_0.5V", format="pdf")
# %%
