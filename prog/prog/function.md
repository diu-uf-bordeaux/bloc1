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

- L'instruction `return` indique la valeur renvoyée.


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

--

### Fonctions : principes

- Une fonction est un bloc de code **réutilisable**. Sa vocation
  première est de factoriser du code.

- Un programme se découpe naturellement en un ensemble de fonctions
  qui forment une couche d'**abstraction** au
  dessus des instructions élémentaires.

- Il s'agit d'un premier exemple de **modularité**.

--

### Fonctions : types


- Il est naturel d'associer un **type** à une fonction&nbsp;:


- Les types aident à vérifier la composition des fonctions.

- Il est désirable qu'une fonction s'applique au plus grand nombre de
  valeurs possible, e.g. qu'elle soit **générique**.


- Il arrive fréquemment qu'une fonction modifie ses paramètres sans
  renvoyer de résultat.



--

### Fonctions : remarques

- <span class="label">Python</span> Une fonction sans instruction `return`
  renvoie `None`.


--

```python
def uneMinuteEnPlus (h, m):
    if m < 59:
        return (h, m+1)
    elif h < 23:
        return (h+1, 0)
    else:
        return (0, 0)
```

```python
def uneMinuteEnPlus (h, m):
    m = (m + 1)%60
    if m == 0:
        h = (h + 1)%24
    return h, m
```

```python
def uneMinuteEnPlus(h,m):
    return(h+(m+1)//60)%24, (m+1)%60
```


---

### L'appel de fonction

(La vrai pile d'appel)
Règle d'évaluation


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
L = [1,2,3]
def test(L):
    L = L + [4]
test(L)
print(L)
```

- qu'affiche-t-il ?
```python
L = [1,2,3]
def test(L):
    L.append(4)
test(L)
print(L)
```

--


### Formes spéciales

--

Passage par valeur/référence

--

### Retour

Afficher n'est pas retourner
(poil au pied)
