### Instructions

- Un <span class='strong'>bloc</span> est une séquence d'instructions

```python
instruction
statement parameters:
    instruction
    instruction
```

- Les programmes sont structurés en blocs imbriqués de manière arborescente.

- Les blocs servent à structurer un programme.

- En **Python**, les blocs doivent être impérativement au même niveau
  d'indentation.

Note: Python redéfinit la notion de bloc, qui n'est pas la même puisqu'elle ne considère comme bloc que les modules, fonctions et classes.

--

### Portée

- La <span class='strong'>portée</span> d'une variable est la zone du programme depuis
  laquelle elle est accessible.

- Une variable définie dans un bloc est accessible depuis ce bloc et
  les blocs imbriqués.

```python
i = 3
while i != 0:
    i = i - 1
```

--

- Accéder au contenu d'une variable non initialisée mène à une erreur.

```python
u = u - 1
# NameError: name 'u' is not defined
```

- En Python, il n'est pas possible de modifier une référence externe à
  une fonction, un module ou une classe.

```python
i = 0
def func():
    i = i - 1 # modify external variable
func()
# UnboundLocalError: local variable 'i' referenced before assignment
```


--

### Conditionnelle

- L'instruction de branchement s'écrit <span class='strong'>if .. else</span> :

```python
if condition:
    block_true
else:
    block_false
```

- Ici, `condition` est une expression booléenne (and, or, not,
comparaisons ...)

<div class='float2'>

en Python  <!-- .element: class="title" -->
```python
if chaperon == rouge:
    open_door()
else:
    ask_again()
```

</div>
<div class='float2'>

en Scheme  <!-- .element: class="title" -->
```scheme
(if (= chaperon rouge)
    (open_door)
    (ask_again))
```

</div>

--

### Boucle non bornée

- Répéter un bloc se fait dans une boucle <span class='strong'>while</span>&nbsp;:

```python
while condition:
    block_while
```

- Attention : engendre facilement des boucles infinies.

- Peut prendre de nombreuses formes selon le langage (loop, repeat .. until, do .. while, ...)

<div class='float2'>

en Python  <!-- .element: class="title" -->
```python
found = False
while not found:
    found = search_more()
```

</div>
<div class='float2'>

en C  <!-- .element: class="title" -->
```c
found = 0; // false
while (!found)
    found = search_more();
```

</div>


--

### Boucle

- `for`

```python
for variable in iterable :
    instructions
```

*iterable* : liste, tuplet, dictionnaire, etc.

- (ajouter un example bien choisi)

- (ajouter un exercice)


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
