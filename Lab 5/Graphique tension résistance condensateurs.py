#%%
from operator import index
from turtle import color, fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

Données = []

for i in range(20):
    a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 5/Labo 5 mesures/Labo 5 Partie 1 resistance avec condensateurs {i+1}.lvm')
    data = a[0]["data"]
    
    R = np.mean(data[:, 0])
    I_R = np.std(data[:, 0])/math.sqrt(30)
    
    V = np.mean(data[:, 1])
    I_V = np.std(data[:, 1])/math.sqrt(30)
    if I_V < 0.0000000001:
        I_V = 0.001

    P = (V**2)/R
    I_P = math.sqrt(2*(I_V/V)**2 + (I_R/R)**2)*P

    mesure = [R, I_R, (P), (I_P)]

    Ajout = True

    for j in Données:
        if j[0] > R:
            Données.insert(Données.index(j), mesure)
            Ajout = False
            break
    if Ajout:
        Données += [mesure]
    #print(f"{i+1} & {R} ± {I_R} & {V} ± {I_V} & {P} ± {I_P}" + "\\" + "\\")

Données = np.array(Données)
print(Données)

Res = (Données[:, 0])
I_Res = (Données[:, 1])
Ten = (Données[:, 2])
I_Ten = (Données[:, 3])

#%%
from scipy import optimize

def Puissance(R_ch, R_s, V_s):
    return (R_ch*(V_s)**2)/((R_ch+R_s)**2)

#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Res_ref = np.linspace(10, 220 , 22000)
Pui_ref = np.linspace(0, 2.2, 22000)

plt.xscale("log")
plt.errorbar(Res, Ten*1000, xerr = I_Res, yerr = I_Ten*1000, mfc = "black", ms = 4, ls = "-", label="Puissance réele")

opt = optimize.curve_fit(Puissance, Res[4:], Ten[4:])
R_s = opt[0][0]
V_s = opt[0][1]
err = np.sqrt(np.diag(opt[1]))
print(f"Résistance de la source: {R_s} ± {err[0]}")
print(f"Tension de la source: {V_s} ± {err[1]}")

ref = Puissance(Res_ref, R_s, V_s)

plt.plot(Res_ref, Puissance(Res_ref, R_s, V_s)*1000, color = "red", ms = 0, ls = "-", label = "Courbe théorique")
plt.plot(Res_ref[list(ref).index(max(ref))]*np.ones(22000), Pui_ref, color="blue", ms = 0, ls = "-", label = f"Résistance de la source")

plt.xlabel("Résistance [Ohm]")
plt.ylabel("Puissance dissipée [mW]")
plt.legend()
#caption = """Figure 2: Puissance en fonction de la résistance totale du circuit (Ohm) dans la circuit sans condensateurs en parallèle"""

#plt.text(0.07, 0.2, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Graphique Puissance Condensateurs.pdf")








# %%
