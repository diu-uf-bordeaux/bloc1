### Nombres entiers

- Représentation canonique en base 2

- Questions de longueur et de représentation

- Le grand mensonge de Python

--
### Opérations élémentaires

- Addition, multiplication (comme à l'école élementaire, mais en plus facile)

- Opérations sont exactes modulo

- <span class="label">Python</span> Les opérations sur les entiers
  sont exactes.

--

### Complément à deux

- Problème de la représentation des entiers signés

- Choix d'une représentation modulo

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

--

### Opérations sur les booléens