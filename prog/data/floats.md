### Nombres flottants

- Représentation normalisée : norme IEEE754

(historique, permet de transposer des calculs indépendamment des
machines qui les font)

- Forme de la représentation sur $n = p + e$ bits.

![IEEE754](data/images/ieee754_repr.png) <!-- .element: class="stretch" style="max-width: 60%;" -->

Sur 32 bits : ![IEEE754](data/images/ieee754_bits.png) <!-- .element: class="stretch" style="max-width: 90%;vertical-align: middle" -->
Note:

Il y a bien p+e bits en tout, même s'il y a un bit de signe. En effet,
sauf pour les nombres spéciaux, le premier bit de la mantisse est
toujours égal à 1, ce qui permet de regagner le bit de signe.


--

### Nombres flottants : types

| Paramètre   | Simple | Double |
|-------------|:------:|:------:|
| p           | 24     | 53     |
| e           | 8      | 11     |
| Total :     | 32     | 64     |
| Exposant :  | -128 à 127 | -1024 à 1023 |
| Décimales : | $\approx 7$ | $\approx 15$ |

--

### Nombres flottants : limites

- Les réels ne sont pas tous représentables exactement.

$$ 0.1 = 0.0001100110011 ... $$

- Les opérations ne sont plus associatives :

![IEEE754](data/images/addition_assoc.png) <!-- .element: class="stretch" style="max-width: 100%; vertical-align:top" -->

- Les erreurs d'approximation ont tendance à s'accumuler.

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

- Ne jamais comparer directement deux nombres flottants.

```python
x == 3.14             # à proscrire
(x - 3.14) < 1e-5     # toujours lama faire comme ça
```

- Éviter de soustraire des quantités équivalentes.

<div class="half">

```python
def quadratic_roots1(a,b,c):
    sq_delta = math.sqrt(b*b - 4*a*c)
    x1 = (- b - sq_delta) / (2 * a)
    x2 = (- b + sq_delta) / (2 * a)
    return (x1,x2)
```

</div>

<div class="half">

```python
def quadratic_roots2(a,b,c):
    sq_delta = math.sqrt(b*b - 4*a*c)
    if b > 0:
        x1 = (- b - sq_delta) / (2 * a)
    else:
        x1 = (- b + sq_delta) / (2 * a)
    x2 = c / (a * x1)
    return (x1,x2)
```

</div>

<div class="half">

```python
quadratic_roots1(1,1e8,1)
# -> (-1e8, -7.450580e-09)  25% error
```

</div>

<div class="half">

```python
quadratic_roots2(1,1e8,1)
# -> (-1e8, -1e-08)      2e-12% error
```

</div>