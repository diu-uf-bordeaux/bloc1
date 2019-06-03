### Blocs d'instructions

- Un <span class='strong'>bloc</span> est une séquence d'instructions :

```python
instruction            #   |a block
statement parameters:  #   |
    instruction        #   |   |a sub-block
    instruction        #   v   v
```

- Un programme est structuré en blocs imbriqués les uns dans les
  autres de manière arborescente.

- Exemples : les boucles, les fonctions, les modules ...

<div class="half">

```python
while condition:
    instruction  # a block
    instruction  #
```

</div>

<div class="half">

```python
def function(args):
    instruction  # a block
    instruction  #
```

</div>

- <span class="label">Python</span> Les instructions d'un bloc doivent
  être au même niveau d'indentation (ou plus profond si sous-blocs).

Note: Python redéfinit la notion de bloc, qui n'est pas la même puisqu'elle ne considère comme bloc que les modules, fonctions et classes.

--

### Portée

- La <span class='strong'>portée</span> d'une variable est la zone du
  programme depuis laquelle elle est accessible.

- Une variable définie dans un bloc est accessible depuis ce bloc et
  les blocs imbriqués.

```python
i = 3                 # variable defined in outer block
def decrease():
    while i != 0:
    	  i = i - 1   # and used inside a sub-block
```

--

### Portée : remarques

- Accéder à une variable non initialisée (ou autrement inaccessible)
  engendre une erreur.

```python
unk = unk + 1
# NameError: name 'unk' is not defined
prrrint("an important message")
# NameError: name 'prrrint' is not defined
```

- <span class="label">Python</span> Il n'est pas possible de modifier
  une référence externe à une fonction, un module ou une classe.

```python
i = 0
def func():
    i = i - 1 # modify external variable
func()
# UnboundLocalError: local variable 'i' referenced before assignment
```

- <span class="label">Python</span> Un bloc ne peut pas être vide
  (cf. instruction `pass`)

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

<div class='half'>

en Python  <!-- .element: class="title" -->
```python
if chaperon == rouge:
    open_door()
else:
    ask_again()
```

</div>
<div class='half'>

en Scheme  <!-- .element: class="title" -->
```scheme
(if (= chaperon rouge)
    (open_door)
    (ask_again)
)
```

</div>

--

### Boucle "Tant Que"

- Répéter un bloc en spécifiant une condition d'arrêt se fait dans une
  boucle <span class='strong'>while</span>&nbsp;:

```python
while condition:
    instructions
    condition = expression    # not compulsory
```

- La boucle est répétée tant que la condition est valide.
(attention : engendre facilement des boucles infinies)

- Peut prendre de nombreuses formes selon le langage (loop, repeat .. until, do .. while, ...)

<div class='half'>

en Python  <!-- .element: class="title" -->
```python
found = False
while not found:
    found = search_more()
```

</div>
<div class='half'>

en C  <!-- .element: class="title" -->
```c
found = 0; // false
while (!found)
    found = search_more();
```

</div>


--

### Boucle "Pour"

- Répéter un bloc en paramétrant chaque tour de boucle se fait à
  l'aide d'une boucle <span class='strong'>for</span>&nbsp;:

```python
for variable in iterable:
    instructions(variable)
```

- La boucle est répétée autant de fois qu'il y a d'éléments dans
  l'itérable.

- Exemples d'itérables : éléments d'une liste, tuple, dictionnaire,
  chaîne de caractères ...

<div class='half'>

en Python  <!-- .element: class="title" -->
```python
sum = 0
for i in range(10):
    sum += i
```

</div>
<div class='half'>

en C  <!-- .element: class="title" -->
```c
int sum = 0;
for (int i=0; i<10; i++)
    sum += i;
```

</div>

--

### Pourquoi ces instructions ?

- Les boucles et les conditionnelles constituent un ensemble minimal
  d'instructions capables d'exprimer n'importe quel programme.

(ça vaut donc le coup d'en parler)

- De nombreuses autres instructions sont construites à partir de ces
  éléments de base.

- Suivant les langages, il existe d'autres types d'instructions ne
  s'exprimant pas avec : programmation logique, programmation
  parallèle, programmation stochastique, programmation quantique ...


--

### Exercice

- Que calcule le code suivant ?

```python
s = 0
n = 2019
while n > 0:
    s = s + 1
    n = n // 2
```

| n     | s |
| :---: |:-:|
| 2019  | 0 |
| 1009  | 1 |
| 504   | 2 |
| ...   | ... |

Note: s = 11 à la fin, et 2^11 == 2048