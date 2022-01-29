#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Fermé-1kOhm_0.05V_28_01_2022.lvm')
Tension = a[0]["data"]*1000
n_bins = 40
dist1 = Tension

plt.hist(dist1, bins=n_bins, color="k")
plt.minorticks_on()
plt.xlabel("Tension mesurée (mV)")
plt.ylabel("Nombre de données")
plt.show
# %%
