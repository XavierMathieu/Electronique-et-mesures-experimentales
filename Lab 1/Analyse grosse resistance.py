"""
Tout fonctionne par cellules dans ce programme si vous avez une 
extension pour le code en Jupyter sur votre éditeur. Chaque
cellule peut donc faire sa fonction séparément des autres, ou on 
peut tout exécuter en même temps! Il faut cependant toujours 
faire exécuter la première en premier pour importer les librairies 
utilisées par les autres cellules plus bas.
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import lvm_read as l

#Attention: utiliser le chemin de votre ordinateur vers le fichier
#de données brutes, disponible sur notre canal teams (même nom de fichier)

a = l.read(rf'C:/DATA/Université/Électronique et mesures/Lab 1/Données brutes Lab1/Labo1_Montage_0.5V_28_01_2022.lvm')
Tensions = a[0]["data"]*1000

#algorithme de tri, on saute les tensions négatives sur R2
V_2 = []
V_T = []
for i in range(len(Tensions[:, 1])):
    if Tensions[:, 1][i] < 0:
        continue
    else:
        V_2 += [Tensions[:, 1][i]]
        V_T += [Tensions[:, 0][i]]
V_R2 = np.array(V_2)
patate = np.array(V_T)

#Enlevez les # de la section suivante 
#pour accéder à la plage de données complète
#(ces lignes écrasent le tri avec la liste complète)

#V_R2 = Tensions[:, 1]
#patate = Tensions[:, 0]

#le calcul en tant que tel
I = V_R2/12
V_R1 = patate - V_R2

R1 = V_R1 / I

# %%
#ici on trouve les différents paramètres
#pour l'analyse statistique
moy = np.mean(R1)
print(f"La moyenne est {moy}!")

med = np.median(R1)
print(f"La médiane est {med}!")

eqt = np.std(R1)
print(f"L'équart type est {eqt}!")

maxi = np.amax(R1)
print(f"Le maximum est {maxi}!")

mini = np.amin(R1)
print(f"Le minimum est {mini}!")

# %%
#petit graphique rapide pour voir l'apparence des résultats
fig=plt.figure(figsize=(6.4, 4.8*1.2))
fig.subplots_adjust(bottom=0.3)

plt.hist(R1, bins=100, edgecolor='black', facecolor="lightgrey")
plt.minorticks_on()
plt.xlabel("Résistance")
plt.ylabel("Nombre de données")
plt.show
# %%
