# MGA802_municipalites

Exercice portant sur l'évolution de la population dans les municipalités du Québec d'après les données issues du
gouvernement provincial.  

## Fonctionnement

1. **Prérequis :** Assurez-vous d'avoir installé Python 3 ainsi que les bibliothèques pandas et matplotlib.

2. **Fichier de données :** Assurez-vous d'avoir le fichier CSV "Census_2016_2021.csv" contenant les données du recensement.
Celui-ci est inclu avec les fichiers de téléchargement sur ce repo GitHub

3. **Exécution :** Lancez le programme en exécutant le fichier principal `main.py`.

4. **Fonctionnement :**
   - Lecture des données du fichier CSV et création d'un DataFrame les regroupant
   - Filtrage pour ne conserver que les municipalités.
   - Calcul du nombre total de municipalités au Québec.
   - Calcul de la population moyenne et du pourcentage d'accroissement.
   - Visualisation de l'évolution de la population à l'aide de pyplot.
   - Classement des municipalités par taille de population et création de series.
   - Visualisation de la répartition des municipalités par taille à partir d'un DataFrame regroupant les series.

## Structure du Code

- `main.py` : Fichier principal contenant le code Python.
- `Census_2016_2021.csv` : Fichier CSV contenant les données du recensement.
- `README.md` : Ce fichier expliquant le fonctionnement du programme, rédigé avec l'aide de ChatGPT avec le prompt :   
"Rédige un document README.md en MarkDown en respectant les standards de l'industrie pour présenter ce code à l'utilisateur (indication de son fonctionnement etc...)".
