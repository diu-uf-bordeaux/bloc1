### Collections

- Une **collection** est un type de données permettant de regrouper
  des données.

- <span class="label">Python</span> <a href="#/expression">Exemples</a> :
  **listes**, **tuples**, **dictionnaires**, **ensembles** ...

- Les collections sont itérables.

- Elles peuvent être mutables ou immutables.

- Elles présentent des interfaces de programmation et des propriétés
  algorithmiques différentes.

- Certains langages ne font la promotion que d'un type de collection :
  les tableaux <span class="label">C</span>, les listes <span
  class="label">Scheme</span>.

--

### Listes (Python)

- La collection le plus utilisée en Python :

<div class="half">

```python
arr = [1, 2, 3, 5]
len(arr)            # 4
3 in arr            # -> True
```

</div>

<div class="half">

```python
for a in arr:
    print(a)
# affiche 1, 2, 3 et enfin 5
```

</div>


- Algorithmiquement, cumule les traits à la fois :

    - d'un tableau (à la **C**)
    - d'une liste (à la **Scheme**)

- Il s'agit d'un conteneur mutable.

- Il sert usuellement à stocker des données d'un seul type.

- Interface riche aux propriétés
  [algorithmiques](https://wiki.python.org/moin/TimeComplexity)
  connues.

Note:
Il y a aussi des array en Python, mais ce sont des formes
particulières des listes Python.
Et non, on n'a pas dit que les listes étaient hétérogènes avant.

--

### Les listes Python sont des tableaux

- Accès **aléatoire** (ou aussi **direct**) à n'importe quel élément
  du tableau (en lecture et écriture) :

```python
tab = [3, 1, 4, 1, 5, 92]
tab[5]                     # -> 92
tab[5] = 9265              # tab == [3, 1, 4, 1, 5, 9265]
```

- En <span class="label">C</span>, les tableaux ont une taille fixe,
  et donc une représentation en mémoire simple.

- Exemples d'utilisation : matrice, image

--

### Les listes Python sont des listes

- **Ajout** et **retrait** à la fin se font en temps constant :

```python
tab = [3, 1, 4, 1, 5, 92]
tab.append(7)              # tab == [3, 1, 4, 1, 5, 92, 7]
tab.pop()                  # -> 7
                           # tab == [3, 1, 4, 1, 5, 92]
```

- Possibilité de concaténer (`+`) et d'inverser l'ordre (`reverse`)
  des éléments d'une liste.

- Exemple d'utilisation : algorithmes récursifs

Note:
Algo récursif -- head, *tail = [1, 1, 2, 3, 5]
Dire qu'il existe d'autres méthodes sur les listes, qu'elles sont de
complexité différentes (usuellement non constante) mais qu'elles
permettent d'écrire des algorithmes plus facilement.

--

## Listes : constructions possibles

- De manière explicite :

```python
l1 = [3, 1, 4, 1, 5, 92]
```

- En étendant par concaténation :

```python
l1 = l1 + [17]      # équivalent à l1.append(17), à l1 += [17]?
l1 = l1 + [20, 2]   # équivalent à l1.extend([20, 2])?
l2 = [0]*10
```

- En étendant par insertion :

```python
l1.insert(4, 12)
l1[3:3] = [10, 10, 10]
```

- En tant que sous-liste :

```python
l3 = l1[5:10]
```

- Comme une <a href="#/comprehensions">compréhension de liste</a>.

--

### Liste : copie

copie **superficielle** vs copie **profonde**

- la modification de l2 affecte-t-elle l1 ?

```python
l1 = [10, 20, 30, 40, 50, 60]
l2 = l1
l2[1] = 0
```


```python
l1 = [10, 20, 30, 40, 50, 60]
l2 = l1.copy()
l2[1] = 0
```

```python
l1 = [[10, 20], [30, 40], [50, 60]]
l2 = l1.copy()
l2[1] [1] = 0
```

--

### Tuples

- Collection **immutable** et hétérogène.

```python
rv = ("Luke", date(3280, 1, 1), "Object: discuss with son")
len(rv)              # -> 3
rv[0]                # -> "Luke"
rv[1] = date.today() # erreur : un tuple est immutable
"Luke" in rv         # -> True
```

- Exemple d'utilisation : manipulation de données hétérogènes, retour
  multiple de fonction, swap

Note:
Appel de fonction ?

--

### Dictionnaires

- Collection **mutable** aussi appelée **tableau associatif**.
  Permet d'associer des **clés** à des **valeurs**.

- Exemple : les clés sont des chaînes, les valeurs des entiers.

```python
pills = { "red": 1, "blue": 1, "pink": 0 }
pills["red"]       # -> 1
pills["pink"]      # -> 0
"blue" in pills    # -> True
"green" in pills   # -> False
pills["green"] = 2 # pills == {'red':1, 'blue':1, 'pink':0, 'green':2}

```

<div class="half">

Itérer sur les clés  <!-- .element: class="title" -->
```python
for k in pills:
    print(k, pills[k])
```

</div>
<div class="half">

Itérer sur tout  <!-- .element: class="title" -->
```python
for k, v in pills.items():
    print(k, v)
```


</div>

- Exemple d'utilisation : données hétérogènes nommées (carnet
  d'adresse), données avec indexation non entière
