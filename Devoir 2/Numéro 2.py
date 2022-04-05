#%%
from turtle import fillcolor
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l
import math

def G_w(w):
    Re = 28.2*(10**(-12)) - 5875.2*(w**2)
    Im = 824400000*w - 0.011664*(w**3)
    a = 3*(w**2)*Re - 500000*Im
    b = 500000*Re + 3*(w**2)*Im
    return (324*np.sqrt(a**2 + b**2))/(Re**2 + Im**2)



#%%
W_1 = np.linspace(0, 10, 1001)
W_2 = np.linspace(10, 10000000, 9999991)
Db = np.linspace(-70, 30, 1000)
ref_1 = G_w(W_1)
W_max_1 = W_1[list(ref_1).index(max(ref_1))]
ref_2 = G_w(W_2)
W_max_2 = W_2[list(ref_2).index(max(ref_2))]
print(W_max_1)
print(W_max_2)

#%%
test = np.round(ref_2, 5)
val = round(max(test)*(2**(-0.5)), 5)
W_coup_1 = W_2[list(test).index(val)]
test_2 = test[::-1]
W_coup_2 = W_2[-list(test_2).index(val)]
print(W_coup_1)
print(W_coup_2)

#%%
plt.style.use('https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle')
fig=plt.figure(figsize=(6.4, 4.8*1.2))
#fig.subplots_adjust(bottom=0.3)
plt.xscale("log")
plt.ylim(-70, 50)
#plt.plot(W, 20*np.log10(G_w(W)), ls = '-', ms = 0, label="Gain")
plt.plot(W_1, 20*np.log10(ref_1), ls = '-', ms = 0, label="Gain")
plt.plot(W_2, 20*np.log10(ref_2), ls = '-', ms = 0)
plt.plot(W_max_2*np.ones(1000), Db, color="blue", ms = 0, ls = "-", label="Fréquence de résonnance")
plt.plot(W_coup_1*np.ones(1000), Db, color="red", ms = 0, ls = "-" , label="Fréquences de coupure")
plt.plot(W_coup_2*np.ones(1000), Db, color="red", ms = 0, ls = "-")
#plt.plot(np.linspace(0, 10000000, 1000), (max(ref_1)-3)*np.ones(1000), color="green", ms = 0, ls = "-")
plt.xlabel("Fréquence (rad/s)")
plt.ylabel("Gain [dB]")
plt.legend()
#plt.text(0.1, 0.15, caption, fontsize='x-large', verticalalignment='top', transform=plt.gcf().transFigure)

plt.show
#plt.savefig(rf"C:/DATA/Université/Électronique et mesures/Devoir 2 numéro 2.pdf")
# %%

