### Compréhensions de listes

- Syntaxe

- Map, filter

- Facilite les transformations sur les itérables

--

### Compréhensions : exemples

- map sur square

- filter sur even

--

### Exceptions

- `try` enregistre une barrière dans la pile d'appel, `except` défini le type
  des exceptions traitées (`else` tout le reste).

- `raise` lève une exception qui deroule la pile d'appel jusqu'a la premiere
  barriere qui sait la traiter.

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

--

### Itération

- Après le `in`, n'importe quelle valeur itérable est possible:
  - une valeur qui défini l'opérateur `__iter__`
  - dont la valeur retournée par est un itérateur

- Un itérateur défini l'operateur `__next__`
  - Qui retourne l'élement suivant de la séquence
  - Lève `StopIteration`
  - Est son propre itérable

<div class="half">

~~~python
for i in something():
  print(i)
~~~

</div>
<div class="half">

~~~python
iterator = iter(something())
try:
  while True:
    i = next(iterator)
    print(i)
except StopException:
  pass
~~~

</div>

Note:
C'est pas exactement vrai, il peut y avoir `__get_item__`, etc

--

### Exemple d'iterateur

<div class="half" style='width:46%;'>

~~~python
class Countdown:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == 0:
            raise StopIteration
        self.value -= 1
        return self.value

for i in Countdown(20)
    print(i)
~~~

</div>
<div class="half" style='width:53%;'>

~~~python
class FilterEven:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            val = next(self.iterator)
            if val % 2 == 0:
                return val


for i in FilterEven(Countdown(20)):
    print(i)
~~~

</div>


--

### Générateur

- Utiliser `yield` dans le corps d'une fonction, transforme la fonction en générateur.

- Le resultat de l'appel de fonction est un itérable, i.e., compatible avec `for`
- Chaque appel à l'operateur `next`, reprend l'execution du corps jusqu'au `yield` -- qui retourne la valeur
- `return` ou la fin de fonction termine l'execution

--

<div class="half">

~~~python
def countdown(value):
    while value > 0:
        value = value - 1
        yield value
~~~

</div>
<div class="half">

~~~python
def filterEven(iterable):
    iterator = iter(iterable)
    while True:
        try:
            value = next(iterator)
        except StopIteration:
            return
        if value % 2 == 0:
            yield value
~~~

</div>
