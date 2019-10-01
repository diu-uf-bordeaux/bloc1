### Variables

- Une **variable** est un espace mémoire nommé qui **référence** une
  valeur.

- <span class="label">Python</span> L'espace utilisé pour `x` peut
  être identifié par `id(x)`.

- <span class="label">Python</span> La déclaration des variables est implicite.

- L'**affectation** stocke en mémoire la valeur de l'expression affectée :

```python
foo = 2 * 3          # foo contient 6
```

- L'**évaluation** renvoie la valeur actuellement référencée. \

```python
36 + foo             # s'évalue à 42
```

--

### Variables : aliasing

#### En Python, tout est référence

- L'**aliasing** consiste à donner plusieurs noms à un même objet.
  Après `x = y`, `x` et `y` représentent le même objet (même id).

- Après `x = y + z`, on crée un nouvel objet `x` de valeur `y + z`

- Après `x.method(...)` ou `x[...] = ...`  la valeur de `x` peut être
modifiée mais `x` ne change pas d’id.

- Avec des valeurs immutables (nombres, tuples, chaînes), seule
  l’affectation peut modifier une variable. \
  $\Rightarrow$ l'aliasing se fait sans risque.



--

### Variables : exemples

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

```python
m = [[0]*2]*2        # -> [[0 , 0] , [0 , 0]]
id(m[0]) == id(m[1]) # -> True (c'est une copie !)
m[0][0] = 1          #
m                    # -> [[1 , 0] , [1 , 0]]
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
