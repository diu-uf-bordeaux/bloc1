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

### Compréhensions de listes

- Les compréhensions de listes sont une facilité de syntaxe permettant
  de construire et de transformer des listes.

```python
[expression(name) for name in iterable]

```

- Syntaxe proche de l'écriture mathématique classique des ensembles.


<div class="half" style="width:55%">

```python
[ x*x for x in range(6)]
[ x for x in range(6) if x%2 == 0 ]
```

</div>

<div class="half" style="width:43%">

![Tiobe'18](prog/images/comprehensions.png) <!-- .element:  style="max-width: 80%;margin-top: 0px" -->

</div>


- Simplifie l'écriture des **maps** (transformation des éléments un à
  un) et des **filtres** (sélection d'un sous-ensemble).

--

### Compréhensions : exemples

```python
people = [("Thalès",-625,-547), ("Archimède",-287,-212),
          ("Épicure",-331,-270), ("Pythagore",-580,-495),
          ("Socrate",-470,-399), ("Platon",-428,-347) ]
```

- Quelle est la liste des âges de ces illustres personnes ?

```python
ages = [ p[2]-p[1] for p in people ]
```
<!-- .element: class="fragment" data-fragment-index="1" -->

- Quels sont ceux dont le nom commence par un "P" ?

```python
p_people = [ p for p in people if p[0].startswith("P") ]
```
<!-- .element: class="fragment" data-fragment-index="2" -->

- Quel est le plus vieux d'entre eux à sa mort ?

```python
oldest = max([ (p,p[2]-p[1]) for p in people ], key=lambda d: d[1])[0]
```
<!-- .element: class="fragment" data-fragment-index="3" -->

--

### Pour s'entraîner ...

Le <a href="#/tp_classification">lien suivant</a> amène à une annexe
illustrant les concepts vus jusqu'à présent.