### Instruction

- Bloc
- Portée

--

### Liste d'instructions

- `if`

```python
if x == 2:
    x = x - 1
```

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

*condition* : une expression booléenne

and, or, not, comparaisons, in


--

- `for`

```python
for variable in iterable :
    instructions
```

*iterable* : liste, tuplet, dictionnaire, etc.

- (ajouter un example bien choisi)

- (ajouter un exercice)

--

- `while`

```python
while x > 0 :
    x = x - 1
```

```python
while condition :
    instructions
```

--

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


Remarque: bloc ne peut pas être vide `pass`
