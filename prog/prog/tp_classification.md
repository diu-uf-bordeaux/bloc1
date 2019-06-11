### Classification de données

- Informations liées au dépistage de la maladie d'Alzheimer sur
une cohorte de 366 personnes.

- Pour chaque personne :

  - classe `"AD"` (malade) ou `"CN"` (non malade)
  - genre
  - âge
  - score cognitif
  - volume de l'hippocampe en cm3
  - volume de l'hippocampe / volume cérébral total.

--

### Importer les données

- Récupérez le fichier [exo_alzheimer_data.py](prog/exo_alzheimer_data.py)

Il a été construit à partir du fichier csv [suivant](prog/Alzheimer.csv)

- Importez les données avec le code suivant :

```python
import alzheimer_data

data = import_data()
```

- Que pouvez-vous dire de la variable `data` ?

--

### Manipuler une colonne d'une table 2D

- Exercice : pour chaque descripteur numérique, trouver valeur
  minimum, valeur maximum et moyenne

- Contrainte : construire la liste qui correspond à un unique
  descripteur (extraction d'une colonne)

  - En utilisant une boucle `for` et `append`
  - En utilisant une construction de liste par compréhension


Note:
parcours indicé, construction de liste

--

### Sélection de lignes dans une table 2D

Application : séparer l'échantillon en deux groupes

- Exercice : pour chaque descripteur numérique, trouver valeur minimum, valeur maximum et moyenne de chacune des deux classes (malade / non malade).

- Exercice : séparer aléatoirement l'échantillon en deux groupes distincts

  - écrire une fonction qui construit une sous liste d'une liste partir des indices des éléments à conserver

  - utiliser la fonction `shuffle` du module `random`

  - vérifier si les deux groupes contiennent chacun des données appartenant aux deux classes

Note:
tranches de listes, compréhension avec if

--

### Trier les données d'une table 2D


- Exercice : trier la table `data` suivant les scores cognitifs croissants
  - utiliser la fonction `sort` des listes

- Exercice : tester si ce tri a permis de séparer la table suivant les deux classes (groupe "AD" au début)

Note:
Ecriture d'une lambda

--

### Classification utilisant un seul descripteur

- Séparer les données en 2 groupes : \
données d'entrainement et données de test

- Calculer $m_{AD}$ (resp. $m_{CN}$ ) la moyenne du descripteur sur
  les données d'entraînement pour le groupe "AD" (resp. "CN")

- Toute nouvelle donnée (descripteur = $d$) est classée dans le groupe
  "AD" si $d$ est plus proche de $m_{AD}$ que de $m_{CN}$

--

### Evaluation de la qualité de la classification

- Calculer la classe de chaque donnée de test

- Comparer la classe calculée et la classe obtenue de façon à obtenir un taux d'erreur

- Application : trouver quel est le  descripteur le plus pertinent pour diagnostiquer automatiquement la maladie d'Alzheimer
