### Nombres entiers

- Représentation canonique en base 2.

  Sur $n$ bits, on code les entiers de $0$ à $2^{n}-1$.


![entier 8 bits](data/images/integer_repr.png)
  <!-- .element: class="stretch" style="max-width: 60%" -->

- Questions de longueur et de représentation : les entiers peuvent être représentés sur 8, 16, 32, 64 bits ...

- Le grand mensonge de Python : les entiers sont de longueurs
  arbitraires.

Note:
Et donc rend assez difficile de parler de représentation binaire modulo.

--
### Opérations élémentaires

- Addition, multiplication (comme à l'école élementaire, mais en plus facile)

<div class="half">

![addition entier 6bits](data/images/integer_addition.png)
  <!-- .element: class="stretch" style="max-width: 80%" -->

</div>

<div class="half">

![multiplication entier 6bits](data/images/integer_multiplication.png)
  <!-- .element: class="stretch" style="max-width: 85%" -->

</div>

- Opérations `+`, `-` et `*` sont exactes modulo $2^n$.

- La division `//` effectue des arrondis&nbsp;: `7 // 3 == 2`  \
  <span class="label">Python</span> Attention avec les négatifs &nbsp;: `(-7) // 3 == -3 `

Note:
L'addition représente 22 + 49 = 71 = 7 (64)
La multiplication représente 22 * 5 = 110 = 46 (64)

--

### Complément à deux

- Problème de la représentation des entiers signés

- Choix d'une représentation modulo : le **complément à 2**.

  Sur $n$ bits, on code les entiers de $-2^{n-1}$ à $2^{n-1}-1$

- Opérations pour calculer l'opposé d'un nombre :

![complément à deux](data/images/integer_complement.png)
  <!-- .element: class="stretch" style="max-width: 100%" -->

--

### Entiers : exemples

- Manipulation avec Numpy

```python
i = np.uint32(2**32-1) # 4294967295
np.binary_repr(i)      # '11111111111111111111111111111111'
i = i + np.uint32(1)   # 0 (overflow)

```




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

--

### Opérations sur les booléens
