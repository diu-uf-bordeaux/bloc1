### Lambda

- Fonction anonyme, construite à la demande

```python
lambda params_without_parentheses: expression
```

```python
(lambda a,b: a + b)(1,2)                        # -> 3
list(filter(lambda x: x % 2 == 0, range(10)))   # -> [0, 2, 4, 6, 8]
```

- Facilite les techniques de programmation fonctionnelle


---

### Itérateurs

- Retour sur le for
(Comparer au `for` en C/Basic/???)

---

### Compréhensions de listes

- Syntaxe

- Map, reduce, filter