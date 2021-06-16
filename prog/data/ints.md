### Nombres entiers

#### Représentation dans une base

- Un nombre est un nombre, peu importe la base $b$.

$$d_n \times b^n + \dots + d_1 \times b^1 + d_0 \times b^0 \qquad \forall i, d_i \in [0;b[$$

- Il peut s'écrire et s'afficher dans une base quelconque.

```python
bin(42)              # -> '0b101010' (représentation en base 2)
np.base_repr(42, 2)  # -> '101010'   (représentation en base b == 2)
```

- Ou s'écrire directement depuis une autre base que $10$.

```python
0x2a                 # -> 42 (représentation en base 16)
int('101010', 2)     # -> 42 (conversion depuis une chaîne en base 2)
```

--

### Entiers non signés

- Représentation canonique en base 2. \
  Sur $n$ bits, on code les entiers de $0$ à $2^{n}-1$.

![entier 8 bits](data/images/integer_repr.png)
  <!-- .element: class="stretch" style="max-width: 60%" -->

- Questions de longueur et de représentation : les entiers peuvent
  être représentés sur 8, 16, 32, 64 bits ... \
  Ex. de noms de types&nbsp;: `char`, `int`, `unsigned int`, `long` ...

- Particularité <span class="label">Python</span> : les entiers sont
  de longueurs arbitraires.

```python
2 ** 100 # -> 1267650600228229401496703205376 (== 2 puissance 100)

```

Note:
Et donc rend assez difficile de parler de représentation binaire modulo.

--
### Entiers non signés : manipulation

- Utiliser la bibliothèque `numpy` pour manipuler les entiers.

|||
|-|-|
| Entiers non signés sur 8 bits :  | `np.uint8` |
| Entiers non signés sur 32 bits : | `np.uint32` |
| Entiers non signés sur 64 bits : | `np.uint64`|
|||


```python
i = np.uint32(2**32-1)  # 4294967295
np.binary_repr(i)       # '11111111111111111111111111111111'
i = i + np.uint32(1)    # 0 (overflow)
```

- Attention : Python a tendance à convertir les types.

```python
i = np.uint32(2**32-1)  # 4294967295
i = i + 1               # 4294967296 (i est devenu un np.int64)
```

--
### Entiers : Opérations élémentaires

- Addition, multiplication (comme à l'école élémentaire, mais en plus facile)

<div class="half">

![addition entier 6bits](data/images/integer_addition.png)
  <!-- .element: class="stretch" style="max-width: 80%; padding: 0px; margin:0px" -->

</div>

<div class="half">

![multiplication entier 6bits](data/images/integer_multiplication.png)
  <!-- .element: class="stretch" style="max-width: 85%; padding: 0px; margin:-10px" -->

</div>

- Opérations `+`, `-` et `*` sont exactes modulo $2^n$.

- La division `//` est la division euclidienne&nbsp;: `7 // 3 == 2`  \
  <span class="label">Python</span> Attention avec les négatifs &nbsp;: `(-7) // 3 == -3 `

Note:
L'addition représente 22 + 49 = 71 = 7 (64)
La multiplication représente 22 * 5 = 110 = 46 (64)

--

### Entiers signés : complément à deux

- Problème de la représentation des entiers signés : lesquels ?

- Choix d'une représentation modulo : le **complément à 2**.

  Sur $n$ bits, on code les entiers de $-2^{n-1}$ à $2^{n-1}-1$

- Opérations pour calculer l'opposé d'un nombre :

![complément à deux](data/images/integer_complement.png)
  <!-- .element: class="stretch" style="max-width: 100%" -->

```python
~42 + 1 # Calcul du complément à 42 -> -42
```

--

### Entiers signés : manipulation

- Manipulation avec Numpy

|||
|-|-|
| Entiers signés sur 8 bits :  | `np.int8` |
| Entiers signés sur 32 bits : | `np.int32` |
| Entiers signés sur 64 bits : | `np.int64`|
|||


```python
i = np.int32(2**31-1)  # 2147483647
np.binary_repr(i)      # '11111111111111111111111111111111' (que 31 '1')
i = i + np.int32(1)    # -2147483648 (overflow)
np.binary_repr(i)      # '-b10000000000000000000000000000000'
```

Note:

np.binary_repr prend un argument optionnel qui devrait être la taille
du type, mais ce comportement est déprécié depuis quelques versions,
mieux vaut ne pas le montrer. Oui, les affichages sont un peu bizarres.

--

### Exemple de fonction sur les entiers

- Écrire une fonction `convert` qui prend en paramètre un entier $n$
  positif et le convertit en base $b$ en produisant la liste de ses
  décimales&nbsp;:

```python
def convert(n, b):
    res = []
    while n > 0:
        res.append(n % b)
        n = n // b
    res.reverse()
    return res
```
<!-- .element: class="fragment" data-fragment-index="1" -->

```python
convert(42, 2)    # [1, 0, 1, 0, 1, 0]
convert(42, 8)    # [5, 2]
```
<!-- .element: class="fragment" data-fragment-index="1" -->

--

### Et les booléens dans l'histoire ?

- En Python, les booléens sont des entiers particuliers.

```python
True == 1, False == 0      # Both statements are True in Python
```

- En fait, toute valeur Python [a un sens](https://docs.python.org/3.7/library/stdtypes.html#truth-value-testing) en tant que booléen.

|||
|--|--|
|`True`|valeurs $\neq 0$, conteneurs non vides|
|`False`|valeurs $\equiv 0$, conteneurs vides (`[]`, `{}`)|
||||

- Les booléens ont une place particulière en informatique, permettant
  de réaliser des calculs de **logique**.

- Ex. d'application : instruction conditionnelle, électronique
  numérique, bitboards ...

--

### Opérations sur les booléens

|||
|--|--|
|opérateurs logiques    |`and`, `or`, `not`              |
|comparaisons           |`<`, `<=`, `>`, `>=`, `==`, `!=`|
|tests d'identité       |`is`, `is not`                  |
|opérateurs sur les bits|`&`, `\|`, `^`, `~`, `<<`, `>>`  |
||||


```python
6 * 7 == 42      # True (attention, il y a 2 '=' !)
arr = [1,2]
arr.remove(1)
arr == [2]       # True  (même contenu)
arr is [2]       # False (deux tableaux différents)
1 << 10          # -> 2**10 == 1024
x | (1 << 10)    # Force le 10ème bit de x à `1`
```

--

### Recettes de cuisines sur les bits

|||
|--|--|--|
| `&` | sélectionner un bit | `x & READ`
| `\|` | Forcer des bits à 1 | `READ \| WRITE`
| `&~` | Forcer des bits à 0 | `x &~ WRITE`
| `^` | Inversion partielle | `x ^ (READ|WRITE)`
| `1 <<` | Placer un bits à p | `1 << (p - 1)`
|      | Fabriquer `n` 1 | `1 << (n - 1)`
| `&-` | trouver le bit de poids le plus faible | `x &- x`

Note:
- != 0 droit de lecture
- Lecture ET écriture
- Enlever WRITE
- Inverser read et write en même temps (ex vraiment stupide :))
