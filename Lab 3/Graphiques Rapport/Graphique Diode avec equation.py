#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
import lvm_read as l


a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 3/Mesures Lab 3/Labo3_partie3-diode_inverse.lvm')
b = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 3/Mesures Lab 3/Labo3_partie3-diode.lvm')
data_1 = a[0]["data"]
data_2 = b[0]["data"]

t_1 = data_1[:, 0]*(-1)
c_1 = data_1[:, 1]*1000

t_2 = data_2[:, 0]
c_2 = data_2[:, 1]*1000

tension = list(t_1)[::-1] + list(t_2)
courant = list(c_1)[::-1] + list(c_2)

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

def Shockley(V, i_0, v_0):
    return i_0*np.exp(V/v_0) - i_0


#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

opt = optimize.curve_fit(Shockley, tension, courant)
i_0 = opt[0][0]
v_0 = opt[0][1]

plt.plot(tension, Shockley(tension, i_0, v_0), color = "red", mfc = "red", ms = 4, ls = "-", label = "Courbe avec Shockley")
plt.errorbar(tension, courant, xerr = incert_V, yerr = incert_I, mfc = "black", ms = 4, ls = "-", label = "Diode réelle")
plt.xlabel("Tension à la source (V)")
plt.ylabel("Courant mesuré (mA)")

caption = """
Figure 3: Courant aux bornes d'une diode (mA)
en fonction de la tension à la source (V) et
courbe ajustée avec l'équation de Shockley.
"""

plt.text(0.1, 0.2, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)
plt.legend()
plt.show

#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Lab 3/Graphique diode Shockley rapport.pdf")

# %%