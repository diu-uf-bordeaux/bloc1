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

![addition entier 6bits](data/images/integer_addition.png)
  <!-- .element: class="stretch" style="max-width: 50%" -->


- Opérations sont exactes modulo

- <span class="label">Python</span> Les opérations sur les entiers
  sont exactes.

--

### Complément à deux

- Problème de la représentation des entiers signés

- Choix d'une représentation modulo : le **complément à 2**.

  Sur $n$ bits, on code les entiers de $-2^{n-1}$ à $2^{n-1}-1$

- Opérations pour calculer l'opposé d'un nombre :

![complément à deux](data/images/integer_complement.png)
  <!-- .element: class="stretch" style="max-width: 100%" -->

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
