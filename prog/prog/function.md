### Fonction

Déclaration/définition/syntaxe

```python
def doubleDeX(x):
    return 2 * x
```

```python
def nom_fonction(paramètres) :
    instructions
```


```python
def factorial(n) :
  """Retourne le produit des entiers de 1 à n"""
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)
```

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
