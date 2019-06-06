### Itération

- Après le `in`, n'importe quelle valeur itérable est possible:
  - une valeur qui défini l'opérateur `__iter__`
  - dont la valeur retournée est un valeur définisant l'operateur `__next__`
    - Qui retourne l'élement suivant de la séquence
    - Lève `StopIteration` sinon
    - Est son propre itérable

<div class="half">

~~~python
for i in something():
  doSomething(i)
~~~

</div>
<div class="half">

~~~python
iterator = iter(something())
try:
    while True:
      i = next(iterator)
      doSomething(i)
except StopException:
    pass
~~~

</div>

Note:
- Les collections sont itérables
- Monde objet : itérateurs
- Monde fonctionnel : générateur
- `__get_item__`

--

### Itération : Outils

- `reversed()` itère à l'envers
- `range()` générère une séquence d'entiers
- `zip()` fabrique un tuple en coévaluant ses paramètres
- `enumérate()` énumère sous forme de tuples `(indice, valeur)`

--

### Générateur

- Utiliser `yield` dans le corps d'une fonction, transforme la fonction en générateur.
- Le resultat de l'appel de fonction est un générateur, itérable, i.e., compatible avec `for`
- Chaque appel à l'operateur `next`, reprend l'execution du corps jusqu'au `yield` -- qui retourne la valeur
- `return`, la fin de fonction, ou lever l'exception `StopIteration` termine l'execution

Note:
Utile pour les listes infinies

--

### Générateur : Exemple

<div class="half">

~~~python
def my_range(start, stop, step=1):
    value = start
    while value != stop:
        yield value
        value += step
~~~

</div>
<div class="half">

```python
def head(iterable, count):
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
for i in head(fibo(), 20):
  print(i)
```

</div><div class="half">

```python
def fibo():
  yield 1
  yield 1
  n_1 = 1
  n_2 = 1
  while True:
    n_2, n_1 = n_1 + n_2, n_2
    yield n_2
```

</div>

--

### Exceptions

- `try` enregistre une barrière dans la pile d'appel, `except` définit le type
  des exceptions traitées (`else` tout le reste).

- `raise` lève une exception qui déroule la pile d'appel jusqu'a la
  première barrière qui sait la traiter.

Mettre des exemples

--

### Exceptions : avertissement

- Attention à la fuite de ressource: `finally` sert à ça.

<div class='half'>

~~~python
with expr as var:
    doSomeStruffs
~~~

</div><div class='half'>

~~~python
temp = expr
try:
  var = temp.__enter__()
  doSomeStuffs
finally:
  temp.__exit__()
~~~

</div>

Note:
Tout ce qui est ouvert doit être fermé.

--

### Lambda

- Fonction anonyme, construite à la demande

```python
lambda params_without_parentheses: expression
```

- Exemples d'utilisation :

```python
plus = lambda a,b: a + b
plus(1,2)                                      # -> 3
list(filter(lambda x: x % 2 == 0, range(10)))  # -> [0 2 4 6 8]
utiliser any
sorted(range(8), key=lambda x: abs(4-x))       # -> [4 3 5 2 6 1 7 0]
```

- Facilite les techniques de programmation fonctionnelle :

    contrôle de l'évaluation / paresse
