### Lambda

- Fonction anonyme, construite à la demande

```python
lambda params_without_parentheses: expression
```

```python
(lambda a, b: a + b)(1, 2)                       # -> 3
list(filter(lambda x: x % 2 == 0, range(10)))   # -> [0, 2, 4, 6, 8]
```

- Facilite les techniques de programmation fonctionnelle

--

### Compréhensions de listes

- Syntaxe

- Map, reduce, filter

---

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
