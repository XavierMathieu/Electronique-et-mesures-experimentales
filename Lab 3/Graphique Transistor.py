#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 3/Mesures Lab 3/Labo3_partie4-Transistor.lvm')
data_0 = a[0]["data"]
tension_0 = data_0[:, 0]
courant_0 = data_0[:, 1]*1000

data_02 = a[1]["data"]
tension_02 = data_02[:, 0]
courant_02 = data_02[:, 1]*1000

data_04 = a[2]["data"]
tension_04 = data_04[:, 0]
courant_04 = data_04[:, 1]*1000

data_06 = a[3]["data"]
tension_06 = data_06[:, 0]
courant_06 = data_06[:, 1]*1000

data_08 = a[4]["data"]
tension_08 = data_08[:, 0]
courant_08 = data_08[:, 1]*1000

data_1 = a[5]["data"]
tension_1 = data_1[:, 0]
courant_1 = data_1[:, 1]*1000

def incertitude_source_6V(tension):
    incert_V = []
    for v in tension:
        incert_V += [0.001*v + 0.005]
    incert_V = np.array(incert_V)


def incertitude_amp_6(courant):
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




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)


plt.errorbar(tension_0, courant_0, xerr = incertitude_source_6V(tension_0), yerr = incertitude_amp_6(courant_0), mfc = "black", ms = 4, ls = "-", label ="Tension à la base de (0 ± 0.02)V")
plt.errorbar(tension_02, courant_02, xerr = incertitude_source_6V(tension_02), yerr = incertitude_amp_6(courant_02), mfc = "red", ms = 4, ls = "-", label ="Tension à la base de (0.2 ± 0.02)V")
plt.errorbar(tension_04, courant_04, xerr = incertitude_source_6V(tension_04), yerr = incertitude_amp_6(courant_04), mfc = "blue", ms = 4, ls = "-", label ="Tension à la base de (0.4 ± 0.02)V")
plt.errorbar(tension_06, courant_06, xerr = incertitude_source_6V(tension_06), yerr = incertitude_amp_6(courant_06), mfc = "green", ms = 4, ls = "-", label ="Tension à la base de (0.6 ± 0.02)V")
plt.errorbar(tension_08, courant_08, xerr = incertitude_source_6V(tension_08), yerr = incertitude_amp_6(courant_08), mfc = "purple", ms = 4, ls = "-", label ="Tension à la base de (0.8 ± 0.02)V")
plt.errorbar(tension_1, courant_1, xerr = incertitude_source_6V(tension_1), yerr = incertitude_amp_6(courant_1), mfc = "orange", ms = 4, ls = "-", label ="Tension à la base de (1 ± 0.02)V")


plt.xlabel("Tension à la source (V)")
plt.ylabel("Courant mesuré (mA)")

caption = """
Figure 6: Courant aux bornes d'un transistor
bipolaire 2219A (mA) en fonction de la tension à
la source (V) et de la tension à la base (V)
"""
plt.legend(fontsize = "small", frameon = False)
plt.text(0.07, 0.2, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 3/Graphique I-V Transistor.pdf")

# %%
