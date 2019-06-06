### Compréhensions de listes

- Syntaxe

- Mettre un for, mettre un if

- Map, filter

- Facilite les transformations sur les itérables

--

### Compréhensions : exemples

- map sur square

- filter sur even

--

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
