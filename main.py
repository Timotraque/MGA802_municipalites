#Fichier principal du programme

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Census_2016_2021.csv")

df_municipalites = df[df['Type'].str.contains("MÉ")]

nbr_municipalites = df_municipalites['Nom'].count()
print(f"Le nombre de municipalités au Québec est : {nbr_municipalites}")

moy_population = pd.concat([df_municipalites['Nom'],(df_municipalites['Pop21'] + df_municipalites['Pop16'])/2], axis=1)
moy_population.rename({0: "Moyenne pop"}, axis="columns", inplace=True)


# Calcul du pourcentage d'accroissement
moy_population["Acroissement"] = (df_municipalites['Pop21'] - df_municipalites['Pop16']) / moy_population["Moyenne pop"]

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

# Classement des municipalités

df_2000 = moy_population["Nom"][moy_population["Moyenne pop"] < 2000]
df_2000.index = range(0, len(df_2000))
df_9999 = moy_population["Nom"][(moy_population["Moyenne pop"] > 1999) & (moy_population["Moyenne pop"] < 10000)]
df_9999.index = range(0, len(df_9999))
df_24999 = moy_population["Nom"][(moy_population["Moyenne pop"] > 9999) & (moy_population["Moyenne pop"] < 25000)]
df_24999.index = range(0, len(df_24999))
df_99999 = moy_population["Nom"][(moy_population["Moyenne pop"] > 24999) & (moy_population["Moyenne pop"] < 100000)]
df_99999.index = range(0, len(df_99999))
df_100000 = moy_population["Nom"][(moy_population["Moyenne pop"] > 9999)]
df_100000.index = range(0, len(df_100000))


df_classement = {"<2000": df_2000,
                 "2000 - 9999": df_9999,
                 "10000 - 24999": df_24999,
                 "25000 - 99999": df_99999,
                 ">100000": df_100000}
df_classement = pd.DataFrame(df_classement)


# Affichage de la répartition des communes en fonction de leur population

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

plt.figure(figsize=(2.97 * 3, 2.1 * 3))
plt.barh(df_classement.columns, len(df_classement) - (df_classement.isna().sum()))
plt.xlabel('Nombre de communes')
plt.ylabel('Taille des communes')
plt.title("Taille des municipalités du Québec")
plt.show()



