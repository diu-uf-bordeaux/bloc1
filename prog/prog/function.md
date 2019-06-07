### Fonction

- Une **fonction** est un bloc d'instructions paramétré par des
  arguments et renvoyant une valeur&nbsp;:

```python
def function(parameters):
    """documentation"""     # fortement recommandé
    instructions
    return expression       # pour renvoyer une valeur
```

- Le bloc d'instructions est le **corps** de la fonction.

- Les paramètres sont des variables classiques utilisables dans le
  corps de la fonction.

- L'instruction `return` indique la valeur renvoyée \
  (`None` en cas d'absence).

Note:
Les parametres sont des variables dont la valeur initiale est determinée par
l'appel de fonction

--

### Fonction : exemple simple

```python
def is_palindrom(s):
    """Teste si la chaîne `s` est symétrique."""
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True
```


- Tests
<!-- .element: class="fragment" data-fragment-index="1" -->

```python
is_palindrom("abc")                    # -> False
is_palindrom("able was I,I saw elba")  # -> True
```
<!-- .element: class="fragment" data-fragment-index="1" -->


Note:
Ne pas préparer un booléen de retour au départ.

--

### L'appel de fonction

- Évaluation d'un appel de fonction

  - Préparation
  - Activation
  - Exécution
  - Retour

- L'expression `f(x)` s'évalue comme l'expression retournée lors de
  l'exécution de `f` dans laquelle le paramètre a été initialisé à la
  valeur de `x`.

> Essayer le débuggueur sur l'expression `fact(2)`.

Note:
A propos du passage par valeur/référence, ici pas de soucis tout est reference.
Mais quand même, certaines valeurs sont immutables, d'autres sont mutables !!!
Dans l'activation, on peut faire remarquer que c'est la que les parametres
nommés son matchés et les valeurs par défaut prises

Exemples possibles :

a = 1
def plus(a, b):   # Permet de voir les renommages
    return a + b
c = plus(3*a, a)

def factorial ...
z = factorial(2)  # Permet de voir les empilements d'appels

Python évalue les paramètres de gauche à droite
Penser à préparer une case spéciale pour le retour
Préparation : évaluation des paramètres
Activation : binding paramètre variables
Exécution : ...
Retour : remplir la case de retour


--

### Fonction : exemple itératif

```python
def pgcd(a, b):
    """Retourne le PGCD des entiers `a` et `b`."""
     while b > 0:
          tmp = a
          a = b
          b = tmp % b
     return a
```

<div class="half">

en C  <!-- .element: class="title" -->
```c
// Retourne le pgcd de 2 entiers
int pgcd(int a, int b) {
  int r;
  while (b != 0) {
      r = a%b;
      a = b;
      b = r;
    }
  return a;
}
```

</div>

<div class="half">

en Scheme  <!-- .element: class="title" -->
```scheme
;; Retourne le pgcd de 2 entiers
(define (pgcd n p)
   (cond [(< n p) (pgcd p n)]
       [(zero? (rem n p)) p]
       [else (pgcd p (rem n p))]))
```

</div>


Note:
    pgcd(4,6)

--

### Fonction : exemple récursif

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


--

### Portée

- La **portée** d'une variable est la zone du
  programme depuis laquelle elle est accessible.

- L'accessibilité contient typiquement la lecture et l'écriture.

- Une variable définie dans une fonction est accessible dans la
  fonction à partir du moment où elle a été initialisée.

```python
i = 3                 # variable définie dans le module
def update_int():
    j = i + 1         # ok, i est visible depuis la fonction
print(j)              # erreur, j est inaccessible hors de la fonction
# NameError: name 'j' is not defined
```

--

### Portée : remarques

- Accéder à une variable non initialisée (ou autrement inaccessible)
  engendre une erreur.

```python
unk = unk + 1
# NameError: name 'unk' is not defined
prrrint("an important message")
# NameError: name 'prrrint' is not defined
```

- <span class="label">Python</span> Il n'est pas possible de modifier
  une liaison externe à une fonction, un module ou une classe.

```python
str = "a"            # variable définie dans le module
def update_str():
    str = str + "b"  # erreur, modifie la liaison
update_str()
# UnboundLocalError: local variable 'str' referenced before assignment
```


--

### Fonctions : principes

- Une fonction est un bloc de code **réutilisable**. Sa vocation
  première est de factoriser du code.

- Un programme se découpe naturellement en un ensemble de fonctions
  qui forment une couche d'**abstraction** au
  dessus des instructions élémentaires.

- Il s'agit d'un premier exemple de **modularité**.

- Les fonctions sont les éléments de base des techniques de
  programmation fonctionnelle.

--

### Fonctions : conseils

- Réfléchissez aux noms, n'ayez pas peur de renommer.
- Préférez les fonctions courtes.
- Limitez le nombre de paramètres.
- Créez une fonction si vous êtes tentés de :
  - Copier/coller,
  - Commenter (par exemple, un calcul, une condition),
  - Rajouter un niveau d'indentation (pluriel/singulier).
- Si la doc est plus longue que la fonction, il y a probablement
  moyen de subdiviser.
- Ne mélangez jamais les calculs et l'affichage.

--

### Fonctions et spécification

- Il est bon de penser l'écriture des fonctions en ayant en tête la
  **spécification** de son fonctionnement

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
           une liste
       sep
           un séparateur

       Returns
       -------
       str
           le résultat de la concaténation des éléments
           de `lst`, séparés chacun par `sep`.
    """

```

- ... les spécifications aident à la structuration du code.

- Exemple : en terme de **vérification** et de **documentation**.

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


--

### Variables : exercice

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    k = 3
    print(k)
test()
```

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    print(k)
k = 3
test()
```

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    k = k + 1
    print(k)
test()
```

- affiche-t-il 2 ou 3 ?

```python
k = 2
def test():
    k = k + 1
test()
print(k)
```
- affiche-t-il 2 ou 3 ?

```python
k = 2
def test(k):
    k = k + 1
test(k)
print(k)
```


- affiche-t-il 2 ou 3 ?

```python
k = 2
def test(k):
    return k + 1
k = test(k)
print(k)
```

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
