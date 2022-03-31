#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

R = 10000
C = 0.000001
w_c = 1/(R*C)

def G_w_c(w):
    den = 1 + (w/w_c)**2
    return 1/np.sqrt(den)

def P_w_c(w):
    return np.arctan(-w/w_c)

def G_w_r(w):
    den = 1 + (w/w_c)**2
    return (w/w_c)/np.sqrt(den)

def P_w_r(w):
    return np.arctan(1/(w/w_c))


#%%
W = np.linspace(0, 1000000, 1000001)




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(0, 1, 1000)

plt.xscale("log")
plt.plot(W, G_w_c(W), ls = '-', ms = 0, label="Gain")
plt.plot(np.ones(1000)/(R*C), Db, ls = '-', ms = 0, color="red", label="Valeur de 1/RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Gain [-]")
plt.legend()
caption = """Figure 5: Amplitude du signal dans le filtre 
actif passe-bas en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre actif passe-bas amplitude.pdf")




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(-1.5, 0, 1000)

plt.xscale("log")
plt.plot(W, P_w_c(W), ls = '-', ms = 0, label="Gain")
plt.plot(np.ones(1000)/(R*C), Db, ls = '-', ms = 0, color="red", label="Valeur de 1/RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Phase [rad]")
plt.legend()
caption = """Figure 6: Phase du signal dans le filtre 
actif passe-bas en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre actif passe-bas phase.pdf")




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(0, 1, 1000)

plt.xscale("log")
plt.plot(W, G_w_r(W), ls = '-', ms = 0, label="Gain")
plt.plot(np.ones(1000)/(R*C), Db, ls = '-', ms = 0, color="red", label="Valeur de 1/RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Gain [-]")
plt.legend()
caption = """Figure 7: Amplitude du signal dans le filtre 
actif passe-haut en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre actif passe-haut amplitude.pdf")




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(0, 1.5, 1000)

plt.xscale("log")
plt.plot(W, P_w_r(W), ls = '-', ms = 0, label="Gain")
plt.plot(np.ones(1000)/(R*C), Db, ls = '-', ms = 0, color="red", label="Valeur de 1/RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Phase [rad]")
plt.legend()
caption = """Figure 8: Phase du signal dans le filtre 
actif passe-bas en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre actif passe-haut phase.pdf")




# %%
