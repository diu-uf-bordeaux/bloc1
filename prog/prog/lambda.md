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


