### Variable

- Une **variable** est espace mémoire nommé qui **référence** une
  valeur
- <span class="label">Python</span> La déclaration des variables est implicite.
- L'**affectation** stocke en mémoire la valeur de l'expression affectée :
  `foo = 2 * 3`
- L'**évaluation** renvoie la valeur actuellement référencée. \
  `36 + foo`

--

### Exemples

```python
x = 3
y = x + 2
x = 5

isPositive = x > 0   # -> True
areSame = x == y     # -> True

length = 123.456
name = 'Dupont'
adress = "123 rue de Gaulle"

someList = [x, y, 3] # -> [ 5, 5, 3 ]
someList[1] = 10     # -> [ 5, 10, 3 ]
stillSame = x == y   # -> True

x = "Une bien mauvaise idée"
```

--

### Variables : conseils

- Utilisez des noms évocateurs.

- Les variables **doivent** être systématiquement initialisées.

- Une variable commence forcément par une lettre minuscule.

- Il est déconseillé d'utiliser une même variable pour stocker des
  valeurs de types différents.

Note:
Pour les noms: plus c'est global (pour une variable) plus c'est long
(ça mérite d'être explicite).
