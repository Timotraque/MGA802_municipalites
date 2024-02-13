#Fichier principal du programme

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Census_2016_2021.csv")

df_municipalites = df[df['Type'].str.contains("MÉ")]

nbr_municipalites = df_municipalites['Nom'].count()
print(f"Le nombre de municipalités au Québec est : {nbr_municipalites}")

moy_population = pd.concat([df_municipalites['Nom'],(df_municipalites['Pop21'] + df_municipalites['Pop16'])/2], axis=1)
moy_population.rename({0: "Moyenne pop"}, axis="columns", inplace=True)
print(moy_population)

# Calcul du pourcentage d'accroissement
moy_population["Acroissement"] = (df_municipalites['Pop21'] - df_municipalites['Pop16']) / moy_population["Moyenne pop"]
print(moy_population.head())

# Affichage
plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

plt.figure(figsize=(2.97 * 3, 2.1 * 3))
plt.scatter(moy_population.iloc[:, 1] * 100, moy_population.iloc[:, 2] * 100)
plt.xlabel('Population moyenne')
plt.ylabel('Acroissement en %')
plt.title("Evolution de la population des municipalités du Québec")
plt.grid()
plt.show()

