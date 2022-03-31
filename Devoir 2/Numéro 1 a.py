#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

def G_w(w):
    t_1 = 0.00001782*(w**2) + 27135
    t_2 = 0.932805*w
    den = np.sqrt(t_1**2 + t_2**2)
    return (0.27*w)/den


#%%
W = np.linspace(0, 10000000, 10000001)
Db = np.linspace(-100, -15, 1000)
ref = G_w(W)
W_max = W[list(ref).index(max(ref))]
print(W_max)

test = np.round(ref, 5)
val = round(max(test)*(2**(-0.5)), 5)
W_coup_1 = W[list(test).index(val)]
test_2 = test[::-1]
W_coup_2 = W[-list(test_2).index(val)]
print(W_coup_1)
print(W_coup_2)

#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
#fig.subplots_adjust(bottom=0.3)
plt.xscale("log")
plt.plot(W, 20*np.log10(G_w(W)), ls = '-', ms = 0, label="Gain")
plt.plot(W_max*np.ones(1000), Db, color="blue", ms = 0, ls = "-", label="Fréquence de résonnance")
plt.plot(W_coup_1*np.ones(1000), Db, color="red", ms = 0, ls = "-" , label="Fréquences de coupure")
plt.plot(W_coup_2*np.ones(1000), Db, color="red", ms = 0, ls = "-")
#plt.plot(np.linspace(0, 10000000, 1000), (max(20*np.log10(G_w(W)))-3)*np.ones(1000), color="green", ms = 0, ls = "-")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Gain [dB]")
plt.legend()
#plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Devoir 2 numéro 1.pdf")
# %%
