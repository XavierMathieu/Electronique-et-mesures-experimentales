#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

R = 18000
C = 0.000001

def G_w_c(w):
    den = 1 + (R*C*w)**2
    return 1/np.sqrt(den)

def P_w_c(w):
    return np.arctan(-w*R*C)

def G_w_r(w):
    den = 1 + (R*C*w)**2
    return (w*R*C)/np.sqrt(den)

def P_w_r(w):
    return np.arctan(1/(w*R*C))


#%%
W = np.linspace(0, 100, 101)




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(0, 0.2, 1000)

#plt.xscale("log")
plt.plot(W, G_w_c(W)/(2*np.pi), ls = '-', ms = 0, label="Gain")
plt.plot(5*np.ones(1000), Db, ls = '-', ms = 0, color="red", label="Valeur de RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Gain [-]")
plt.legend()
caption = """Figure 1: Amplitude du signal dans le filtre 
passif passe-bas en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre passif passe-bas amplitude.pdf")




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(-1.5, 0, 1000)

plt.xscale("log")
plt.plot(W, P_w_c(W), ls = '-', ms = 0, label="Gain")
plt.plot(5*np.ones(1000), Db, ls = '-', ms = 0, color="red", label="Valeur de RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Phase [rad]")
plt.legend()
caption = """Figure 2: Phase du signal dans le filtre 
passif passe-bas en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre passif passe-bas phase.pdf")




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(0, 1, 1000)

plt.xscale("log")
plt.plot(W, G_w_r(W), ls = '-', ms = 0, label="Gain")
plt.plot(np.ones(1000)/(R*C), Db, ls = '-', ms = 0, color="red", label="Valeur de RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Gain [-]")
plt.legend()
caption = """Figure 3: Amplitude du signal dans le filtre 
passif passe-haut en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre passif passe-haut amplitude.pdf")




#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

Db = np.linspace(0, 1.5, 1000)

plt.xscale("log")
plt.plot(W, P_w_r(W), ls = '-', ms = 0, label="Gain")
plt.plot(np.ones(1000)/(R*C), Db, ls = '-', ms = 0, color="red", label="Valeur de RC")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Phase [rad]")
plt.legend()
caption = """Figure 4: Phase du signal dans le filtre 
passif passe-bas en fonction de sa fréquence
avec C = 0.000 001 Farad et R = 10 000 Ohm"""
plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Filtre passif passe-haut phase.pdf")




# %%