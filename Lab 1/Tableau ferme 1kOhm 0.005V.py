import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Fermé-1kOhm_0.005V_28_01_2022.lvm')
Tension = a[0]["data"]
print(a)
print(Tension)