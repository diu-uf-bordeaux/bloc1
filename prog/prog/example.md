### Programme Python

est une suite d'instructions :

- affectation
```python
x = 3
```
- conditionnelle
```python
if x == 2:
	x = x - 1
```

- boucles
```python
while x > 0 :
	x = x - 1
```


- définition de fonction
```python
def doubleDeX(x):
	return 2 * x
```
- et bien d'autres types

---

### Affectation

```python
nom_variable = expression
```

```python
x = 3
y = x + 2
x = 4
length = 123.456
isPositive = x > 0
name = 'Dupont'
adress = "123 rue de Gaulle"
L = [1, 2, 3]
L[0] = 10
```

--

### Variables

Typage dynamique

liste de types :
- entiers, flottants, booléens, caractères, chaînes de caractères
- fonctions
- types composés : listes, dictionnaires, t-uples, etc.


---

### Conditionnelle

```python
if condition :
	instructions optionnelles
```

```python
if condition :
	branche_Vrai
else :
	branche_Faux
```

```python
if condition_A :
	branche_A
elif condition_B :
	branche_B
else :
	branche_défault
```

*condition* : une expression booléenne

and, or, not, comparaisons, in

---

### Boucle While


```python
while condition :
	instructions
```

<div class='float2'>

que fait le code ?  <!-- .element: class="title" -->
```python
s = 0
n = 2019
while n > 0 :
	s = s + 1
	n = n // 2
```

</div>
<div class='float2'>

et si on faisait ?  <!-- .element: class="title fragment" data-fragment-index="1" -->
```python
s = 0
n = 2019
while n >= 0 :
	s = s + 1
	n = n // 2
```
<!-- .element: class="fragment" data-fragment-index="1" -->

</div>


---

### Boucle For
```python
for variable in iterable :
	instructions
```

*iterable* : liste, tuplet, dictionnaire, etc.

- (ajouter un example bien choisi)

- (ajouter un exercice)

---

### Fonction

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



par valeur, par référence
