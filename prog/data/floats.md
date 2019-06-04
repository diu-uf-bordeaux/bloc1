### Nombres flottants

- Représentation normalisée : norme IEEE754

(historique, permet de transposer des calculs indépendamment des
machines qui les font)

- Forme de la représentation

![IEEE754](data/images/ieee754.png) <!-- .element: class="stretch" style="max-width: 70%;" -->

--

### Nombres flottants : types

- simple precision

- double precision

--

### Nombres flottants : erreurs

Que se passe t'il si l'on additionne plusieurs fois 0.1 sur 32
bits ?

| Valeur réelle  | Valeur flottante      |
| :----: | --------------------- |
| 1/10 | 0.1000000014901161193 |
| 2/10 | 0.2000000029802322387 |
| 3/10 | 0.3000000119209289550 |
| 4/10 | 0.4000000059604644775 |
| 5/10 | 0.5000000000000000000 |

--

### Nombres flottants : principes

- Ne jamais comparer directement deux nombres flottants

```python
x == 3.14             # à proscrire
(x - 3.14) < 1e-5     # toujours lama faire comme ça
```