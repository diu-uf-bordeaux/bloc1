### Exceptions

- `try` enregistre une barrière dans la pile d'appel, `except` définit le type
  des exceptions traitées (`else` tout le reste).

- `raise` lève une exception qui déroule la pile d'appel jusqu'a la
  première barrière qui sait la traiter.

<div class="half">

```python
try:
    mean = sum(arr) / len(arr)
except ZeroDivisionError:
    mean = 0
```

</div>

<div class="half">

```python
try:
    file = open("passwd", "r")
    passwd = file.readline()
except FileNotFoundError:
    passwd = "admin"
```

</div>

Note:
Faire un dessin avec une pile d'appel.

--

### Exceptions : avertissement

- Le mot-clé `finally` permet d'appliquer un traitement à la fin d'un
  bloc `try`, que l'exception soit levée ou pas.

- Un exemple d'utilisation est le cas d'une ressource qui pourrait ne
  pas être libérée à cause d'une exception. \
  Pour éviter la fuite de ressources, il suffit d'utiliser `with`.

<div class='half'>

```python
with expr as var:
    doSomeStruffsThatMayRaiseAnExpetion
```

</div><div class='half'>

```python
temp = expr
try:
  var = temp.__enter__()
  doSomeStruffsThatMayRaiseAnExpetion
finally:
  temp.__exit__()
```

</div>

- Exemples d'objets utilisables avec `with` : fichiers, connections à
  un serveur, verrous de threads ...

Note:
Tout ce qui est ouvert doit être fermé.

--

### Itérables et itérations

- Dans une boucle `for`, après le `in`, n'importe quelle valeur
  itérable est possible.

- Au moment du `for` est construit à partir de l'itérable un objet
  qui répond à la méthode `__next__`.

- À chaque appel, cette méthode `__next__`&nbsp;:
  - retourne l'élément suivant de la séquence, si possible,
  - stoppe la boucle par une exception sinon.

<div class="half">

```python
for i in something():
  doSomething(i)
```

</div>
<div class="half">

```python
iterator = iter(something())
try:
    while True:
      i = next(iterator)
      doSomething(i)
except StopException:
    pass
```

</div>

Note:
- Les collections sont itérables
- Monde objet : itérateurs
- Monde fonctionnel : générateur
- `__get_item__`

--

### Itération : Outils

|||
|--|--|
|`range(start, stop, step)`       | génère une séquence d'entiers |
|`reversed(iter)`                 | itère à l'envers |
|`zip(iter_1, iter_2, .. iter_n)` | itère sur plusieurs itérables simultanément |
| `enumerate(iter)`               | énumère sous forme de tuples `(indice, valeur)` |
|||

--

### Générateur

- Utiliser `yield` dans le corps d'une fonction, transforme la
  fonction en générateur.

- Le resultat de l'appel de fonction est un générateur, itérable,
  i.e., compatible avec `for`.

- Chaque appel à l'operateur `__next__`, reprend l'exécution du corps
  jusqu'au `yield` -- qui retourne la valeur.

- L'instruction `return`, la fin de fonction, ou l'exception
  `StopIteration` termine l'exécution

Note:
Utile pour les listes infinies

--

### Générateur : Exemple

<div class="half">

```python
def my_range(start, stop, step=1):
    value = start
    while value != stop:
        yield value
        value += step
```

</div>
<div class="half">

```python
def take(iterable, count):
    iterator = iter(iterable)
    while count > 0:
        count -= 1
        yield next(iterator)
```

</div>

<div class="half">

```python
def one():
  while True:
    yield 1
```

```python
for i in take(fibo(), 20):
  print(i)
```

</div><div class="half">

```python
def fibo():
  yield 1
  yield 1
  n_1, n_2 = 1, 1
  while True:
    n_2, n_1 = n_1 + n_2, n_2
    yield n_2
```

</div>
