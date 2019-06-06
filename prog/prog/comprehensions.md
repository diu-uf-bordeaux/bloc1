### Compréhensions de listes

- Les compréhensions de listes sont une facilité de syntaxe permettant
  de construire et de transformer des listes.

```python
[expression(name) for name in iterable]

```

- Syntaxe proche de l'écriture mathématique classique des ensembles.

```python
[ x*x for x in range(6)]              # -> [0, 1, 4, 9, 16, 25]
[ x for x in range(6) if x%2 == 0 ]   # -> [0, 2, 4]
```

$$ x^2 \ \textrm{tels que}\ x \in [0;10[ $$

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

- Quels sont ceux dont le nom commence par un "P" ?

```python
p_people = [ p for p in people if p[0].startswith("P") ]
```

- Quel est le plus vieux d'entre eux à sa mort ?

```python
oldest = max([ (p,p[2]-p[1]) for p in people ], key=lambda p: p[1])[0]
```
