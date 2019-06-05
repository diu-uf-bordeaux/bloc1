### Fonction

- Une **fonction** est un bloc d'instructions
  paramétré renvoyant éventuellement une valeur&nbsp;:

```python
def function(parameters):
    """documentation"""     # not compulsory but strongly recommended
    instructions
    return expression       # not compulsory
```

- Le bloc d'instructions est le **corps** de la fonction.

- Les paramètres forment une liste de noms réutilisables dans le
  corps de la fonction.

- L'instruction `return` indique la valeur renvoyée \
  `None` en cas d'absence.

--

### Exemple de fonction

```python
def factorial(n) :
  """Retourne le produit des entiers de 1 à n"""
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)
```

<div class="half">

en C  <!-- .element: class="title" -->
```c
// Retourne le produit des entiers
int factorial(int n) {
  int f;
  for (f = 1; n > 1; n --)
    f *= n;
  return f;
}
```

</div>

<div class="half">

en Scheme  <!-- .element: class="title" -->
```scheme
;; Retourne le produit des entiers
(define (factorial n)
  (if (<= n 0)
      1
      (* n (factorial (- n 1)))))
```

</div>

Note:
Factorial est pas un bon exemple ca fait un appel de fonction avant `l'appel de fonction`

--
### L'appel de fonction

- Une fonction à vocation à être appellée
- Decomposition de l'appel de fonction
  - Préparation
  - Activation
  - Execution
  - Retour (?)
- Sa valeur est celle retournée par l'execution

- Afficher n'est pas retourner (poil au pied)

Note:
A propos du passage par valeur/référence, ici pas de soucis tout est reference.
Mais quand même, il y'a des (rares) objets immutables, les autres le sont !!!

--

### Fonctions : principes

- Une fonction est un bloc de code **réutilisable**. Sa vocation
  première est de factoriser du code.

- Un programme se découpe naturellement en un ensemble de fonctions
  qui forment une couche d'**abstraction** au
  dessus des instructions élémentaires.

- Il s'agit d'un premier exemple de **modularité**.

--

### Fonctions et types

- Même si les types ne sont pas apparents, il est bon de penser
  l'écriture des fonctions en les ayant en tête.

```python
def join(lst, sep):
    """Concatène les éléments d'une liste avec un séparateur"""
    result = lst.pop(0)
    for l in lst:
        result = result + sep + l
    return result
```
- Dans cette fonction &nbsp;:
    -  `lst` est manifestement une liste
    -  `sep` est additionné aux élements de la liste
    - le retour de `join` est le résultat de cette addition

```python
join([1, 2, 3], 0)             # -> 6 (= 1 + 2 + 3)
join(["a", "b", "c"], " and ") # -> "a and b and c"
```


--

- En suivant [des conventions de
  nommage](https://numpydoc.readthedocs.io/en/latest/format.html) ...

```python
def join(lst, sep):
    """Concatène les éléments d'une liste.

       Parameters
       ----------
       lst : list
           une liste de chaînes de caractères
       sep : string
           un séparateur

       Yields
       ------
       str
           la chaîne résultant de la concaténation des élément
           de `lst`, séparés chacun par `sep`.
    """

```

- ... les types aident à la **vérification** et la **documentation**.

- <span class="label">Python $\geq$ 3.5</span>&nbsp; Possibilité d'ajouter
  des annotations de type :

```python
def join(lst: list, sep: str) -> str:
```

--

- Dans des langages aux systèmes de types plus perfectionnés, les
  types permettent aussi de :

    - prévenir des erreurs avant l'exécution du code;

    - optimiser du code suivant sa représentation.

- Néanmoins, ils peuvent être un frein au développement en
  contraignant les possibilités des programmeurs.

    Ainsi, `join` s'applique aussi à des listes de nombres.

--

### Fonctions : exercice

- Écrire une fonction prenant un couple `(h,m)` représentant une heure
  de la journée, et renvoyant le même couple auquel on a ajouté une
  minute.

```python
def uneMinuteEnPlus (h, m):
    """Ajoute une minute au couple (h,m) représentant
       une heure de la journée et renvoie ce nouveau couple."""
    if m < 59:
        return (h, m+1)
    elif h < 23:
        return (h+1, 0)
    else:
        return (0, 0)
```
<!-- .element: class="fragment" data-fragment-index="1" -->


---

--
### Variable locale

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    k = 3
    print(k)
test()
```

--

### Variable locale

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    print(k)
k = 3
test()
```

--

### Variable locale

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    k = k + 1
    print(k)
test()
```

--

### Variable locale


- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    k = k + 1
test()
print(k)
```

--


### Variable locale


- affiche-t-il 2 ou 3 ?

```python
k = 2
def test(k):
    k = k + 1
test(k)
print(k)
```

--

### Variable locale


- affiche-t-il 2 ou 3 ?

```python
k = 2
def test(k):
    return k + 1
k = test(k)
print(k)
```

--


### Variable locale

- qu'affiche-t-il ?

```python
L = [1, 2, 3]
def test(L):
    L = L + [4]
test(L)
print(L)
```

- qu'affiche-t-il ?

```python
L = [1, 2, 3]
def test(L):
    L.append(4)
test(L)
print(L)
```
