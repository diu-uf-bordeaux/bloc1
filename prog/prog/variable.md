### Variable

- Un espace mémoire nommé qui **référence** une valeur
- Déclaration implicite en python
- Affectation stocke la **valeur** du membre droit. \
  `foo = 2 * 3`
- Son évaluation est la valeur actuellement référencée. \
  `36 + foo`

--

### Exemples

```python
x = 3
y = x + 2
x = 5

isPositive = x > 0   # True
areSame = x == y     # True

length = 123.456
name = 'Dupont'
adress = "123 rue de Gaulle"

someList = [x, y, 3] # [ 5, 5, 3 ]
someList[1] = 10
stillSame = x == y   # True

x = "Une bien mauvaise idée"
```
> Limitez au maximum son utilisation polymorphe
