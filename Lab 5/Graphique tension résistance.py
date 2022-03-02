#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

Données = []

for i in range(15):
    a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 5/Labo 5 mesures/Labo 5 Partie 1 resistance seule {i+1}.lvm')
    data = a[0]["data"]
    
    R = np.mean(data[:, 0])
    I_R = np.std(data[:, 0])/math.sqrt(30)
    
    V = np.mean(data[:, 1]*1000)
    I_V = np.std(data[:, 1]*1000)/math.sqrt(30)

    print(f"{R} ± {I_R}, {V} ± {I_V}")
    Données += [[R, I_R, V, I_V]]

Données = np.array(Données)












# %%
