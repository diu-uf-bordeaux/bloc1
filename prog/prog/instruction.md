### Blocs d'instructions

- Un **bloc** est une séquence d'instructions :

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

Note: Python redéfinit la notion de bloc, qui n'est pas la même
puisqu'elle ne considère comme bloc que les modules, fonctions et
classes.

--

### Conditionnelle

- L'instruction de branchement s'écrit `if` .. `else`&nbsp;:

```python
if condition:
    block_true
else:
    block_false
```

- Ici, `condition` est une expression booléenne \
(`and`, `or`, `not`, comparaisons ...)

<div class='half'>

en Python  <!-- .element: class="title" -->
```python
if chaperon == rouge:
    open_door()
else:
    call_for_hunter()
```

</div>
<div class='half'>

en Scheme  <!-- .element: class="title" -->
```scheme
(if (= chaperon rouge)
    (open_door)
    (call_for_hunter))
```

</div>

--

### Boucle "Tant Que"

- Répéter un bloc en spécifiant une condition d'arrêt se fait dans une
  boucle `while`&nbsp;:

```python
while condition:
    instructions
    condition = expression    # pas obligatoire
```

- La boucle est répétée tant que la condition est valide.
(attention : engendre facilement des boucles infinies)

- Peut prendre de nombreuses formes selon le langage (`loop`, `repeat`
  .. `until`, `do` .. `while`, ...)

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
int found = 0; // false
while (!found)
    found = search_more();
```

</div>


--

### Boucle "Pour"

- Répéter un bloc en paramétrant chaque tour de boucle se fait à
  l'aide d'une boucle `for`&nbsp;:

```python
for variable in iterable:
    instructions(variable)
```

- La boucle est répétée autant de fois qu'il y a d'éléments dans
  l'**itérable**, un objet que l'on peut énumérer

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

- Boucles et conditionnelles forment un ensemble **minimal**
  d'instructions pour exprimer **n'importe quel** programme.

(ça vaut donc le coup d'en parler)

- D'autres constructions syntaxiques peuvent être élaborées à partir
  de cette base (e.g. les compréhensions de listes)

- D'autres formes de programmations s'expriment différemment :
  **logique**, **parallèle**, **quantique** ...


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
