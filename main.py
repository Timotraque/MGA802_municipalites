#Fichier principal du programme

import pandas as pd
import numpy as np

df2 = pd.read_csv("Census_2016_2021.csv")

df_municipalites = df2[df2['Type'].str.contains("MÉ")]

nbr_municipalites = df_municipalites['Nom'].count()
print(f"Le nombre de municipalités au Québec est : {nbr_municipalites}")

moy_population = pd.concat([df_municipalites['Nom'],(df_municipalites['Pop21'] + df_municipalites['Pop16'])/2], axis=1)
moy_population.rename({0: "Moyenne pop"}, axis="columns", inplace=True)
print(moy_population)
