### Collections

- C'est quoi une collection ?

- <span class="label">Python</span> Exemples : **listes**, **tuples**,
  **dictionnaires**, **ensembles** ...

- Mutabilité

- Itération

- Interface / Algorithmique

- Certains langages ne font la promotion que d'un type de collection :
  les tableaux en **C**, les listes en **Scheme**.

--

### Listes (Python)

- Le conteneur le plus utilisé en Python : `[1, 2, 3]`.

- Algorithmiquement, cumule les traits à la fois :

    - d'un tableau (à la **C**)

    - d'une liste (à la **Scheme**)


Note:
Il y a aussi des array en Python, mais ce sont des formes
particulières des listes Python.

--

### Les listes Python sont des tableaux

- Accès **aléatoire** ou **direct** à n'importe quel élément du
  tableau (en lecture et écriture) :

```python
tab = [3, 1, 4, 1, 5, 92]
len(tab)                   # -> 6
tab[5]                     # -> 92
tab[5] = 9265              # tab == [3, 1, 4, 1, 5, 9265]
```

- En <span class="label">C</span>, les tableaux ont une taille fixe,
  et donc une représentation en mémoire simple.

- Exemples d'utilisation : matrice, image

--

### Les listes Python sont des listes

- Ajout, retrait, concaténation.

- Exemple d'utilisation : algorithmes récursifs,

Note:
Algo récursif -- head, *tail = [1, 1, 2, 3, 5]

--

### Tuples

- Immutable

- Exemple d'utilisation : retour multiple de fonction

Note:
Appel de fonction ?

--

### Dictionnaires

- Get, Put, iterate key and couples

- Généralise les listes

- Exemple d'utilisation : carnet d'adresse
