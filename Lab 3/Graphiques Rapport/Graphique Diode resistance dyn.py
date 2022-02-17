#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 3/Mesures Lab 3/Labo3_partie3-diode_inverse.lvm')
b = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 3/Mesures Lab 3/Labo3_partie3-diode.lvm')
data_1 = a[0]["data"]
data_2 = b[0]["data"]

t_1 = data_1[:, 0]*(-1)
c_1 = data_1[:, 1]*(1000)

t_2 = data_2[:, 0]
c_2 = data_2[:, 1]*1000

tension = np.append(t_1[::-1], t_2)
courant = abs(np.append(c_1[::-1], c_2))

incert_V = []
for v in tension:
    incert_V += [0.001*v + 0.005]

incert_V = np.array(incert_V)


incert_I = []
for i in courant:
    if i >= 1000:
        incert_I += [0.0012*i + 0.0002*3000]
    elif i >= 100:
        incert_I += [0.001*i + 0.0001*1000]
    elif i >= 10:
        incert_I += [0.0005*i + 0.00005*100]
    else:
        incert_I += [0.0005*i + 0.0002*10]

incert_I = np.array(incert_I)

R_dyn = []
R_dyn_In = []
for j in range(len(tension)-1):
    dI = courant[j+1] - courant[j]
    if dI == 0:
        dI = 0.00000000001

    dV = tension[j+1] - tension[j]
    if dV == 0:
        dV = 0.00000000001
    
    In_dI = incert_I[j+1] + incert_I[j]
    In_dV = incert_V[j+1] + incert_V[j]
    r = dV/(dI*1000)
    incer = (In_dI/dI + In_dV/dV)*r
    if abs(incer) > 1000:
        incer = 0
    R_dyn_In += [incer]
    R_dyn += [r]

print(R_dyn)
print(R_dyn_In)





#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)


#plt.errorbar(tension, courant, xerr = incert_V, yerr = incert_I, mfc = "black", ms = 4, ls = "-")
plt.errorbar(tension[:-1], R_dyn, xerr = incert_V[:-1], ls = "-")
plt.plot
plt.xlabel("Tension à la source (V)")
plt.ylabel("Résistance mesurée (MOhms)")
plt.ylim([-30,30])

caption = """
Figure 4: Courant aux bornes d'une diode (mA)
en fonction de la tension à la source (V) 
"""

plt.text(0.1, 0.2, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 3/Graphique I-V diode.pdf")

# %%