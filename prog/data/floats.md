### Nombres flottants

- Représentation normalisée : norme IEEE754

(historique, permet de transposer des calculs \
indépendamment des machines qui les font)

- Forme de la représentation sur $n = p + e$ bits.

![IEEE754](data/images/ieee754_repr.png) <!-- .element: class="stretch" style="max-width: 60%;" -->

Sur 32 bits : ![IEEE754](data/images/ieee754_bits.png) <!-- .element: class="stretch" style="max-width: 90%;vertical-align: middle" -->
Note:

La norme date de 1985, et est une belle histoire où la standardisation
a uniformisé le paysage de tous les constructeurs.

Il y a bien p+e bits en tout, même s'il y a un bit de signe. En effet,
sauf pour les nombres spéciaux, le premier bit de la mantisse est
toujours égal à 1, ce qui permet de regagner le bit de signe.

--

### Nombre flottants : répartition

<p>&nbsp;<p>

![IEEE754](data/images/ieee754_overview.png) <!-- .element: class="stretch" style="max-width: 100%;" -->

- Chaque point rouge représente un nombre flottant.

Note:

Ce dessin n'est pas entièrement exact, en effet il existe des nombres
flottants dits "dénormalisés" utilisés pour représenter des nombres à
la limite de la zone d'underflow. Il est ainsi possible de grapiller
un peu de précision (de l'ordre du nombre

--

### Nombres flottants : types

| Paramètre   | Simple préc. | Double préc.|
|-------------|:------:|:------:|
| p           | 24     | 53     |
| e           | 8      | 11     |
| Total :     | 32     | 64     |
| Exposant :  | -128 à 127 | -1024 à 1023 |
| Décimales : | $\approx 7$ | $\approx 15$ |
||||

--

### Nombres flottants : nombres spéciaux

- La représentation IEEE754 contient des **nombres spéciaux**&nbsp;:

  - deux zéros, l'un positif `+0.0` et l'autre négatif `-0.0`;

  - deux infinis, l'un positif `+inf` et l'autre négatif `-inf`;

  - une valeur "not a number" `nan` pour les exceptions.

- Avec un certain nombre de règles de calcul particulières&nbsp;:

```python
plus_zero  = np.float32(10**(-128))   # -> 0.0
plus_inf   = 1 / plus_zero            # -> +inf
minus_zero = np.float32(-10**(-128))  # -> -0.0
minus_inf  = 1 / minus_zero           # -> -inf
plus_inf + minus_inf                  # -> nan (warning)
plus_zero / plus_zero                 # -> nan (warning)
```

--

### Nombres flottants : limites

- Les réels ne sont pas tous représentables exactement.

- En fait, tout réel $x$ est approximé par un flottant $rp(x)$&nbsp;:

  $$ rp(x) = (1 + \theta) x \qquad |\theta| \leq \epsilon $$

  où $\epsilon$ est appelé la **précision machine**.

- Sur 32 bits, $\epsilon = 2^{-24}$. Sur 64 bits, $\epsilon = 2^{-53}$.


- Exemple de nombre non représentable exactement&nbsp;:

  $$ \frac{1}{10} = 0.0001100110011 ... $$

--

### Nombres flottants : limites

- Les opérations élémentaires ne sont plus associatives :

![IEEE754](data/images/addition_assoc.png) <!-- .element: class="stretch" style="max-width: 100%; vertical-align:top" -->

  $\Rightarrow$ les résultats des calculs dépendent de l'**ordre** des opérations.

- Les erreurs d'approximation ont tendance à s'accumuler.
  (mais pas de manière systématique)

- Les additions ont tendance à augmenter les erreurs **absolues**, \
  les multiplications à augmenter les erreurs **relatives**.

--

### Nombres flottants : erreurs

Que se passe t'il si l'on additionne plusieurs fois 1/10 sur 32
bits ?

| Valeur réelle  | Valeur flottante sur 64 bits |
| :----: | --------------------- |
| 1/10 | 0.10000000149011612 |
| 2/10 | 0.20000000298023224 |
| 3/10 | 0.30000001192092896 |
| 4/10 | 0.40000000596046450 |
| 5/10 | 0.50000000000000000 |

```python
f32 = np.float32(0.1)
for i in range(5):
    print(np.float64(f32))
    f32 = f32 + np.float32(0.1)
```

--

### Nombres flottants : quelques principes

- Ne jamais comparer directement deux nombres flottants.

```python
x == 3.14             # à proscrire
(x - 3.14) < 1e-5     # toujours lama faire comme ça
```

- Éviter de soustraire des quantités équivalentes.

<div class="half">

```python
def quadratic_roots1(a, b, c):
    sq_delta = math.sqrt(b*b - 4*a*c)
    x1 = (- b - sq_delta) / (2 * a)
    x2 = (- b + sq_delta) / (2 * a)
    return (x1, x2)
```

</div>

<div class="half">

```python
def quadratic_roots2(a, b, c):
    sq_delta = math.sqrt(b*b - 4*a*c)
    if b > 0:
        x1 = (- b - sq_delta) / (2 * a)
    else:
        x1 = (- b + sq_delta) / (2 * a)
    x2 = c / (a * x1)
    return (x1, x2)
```

</div>

<div class="half">

```python
quadratic_roots1(1, 1e8, 1)
# -> (-1e8, -7.450580e-09)  25% error
```

</div>

<div class="half">

```python
quadratic_roots2(1, 1e8, 1)
# -> (-1e8, -1e-08)      2e-12% error
```

</div>

- Eviter de sommer des valeurs d'ordre de grandeur différents.

Note:

Signaler qu'il ne s'agit de que de principes, et pas de règles
absolues. De plus, il est possible d'en imaginer d'autres.

Il existe des notions plus complexes permettant d'évaluer les erreurs
réalisées par chaque calcul, comme le **conditionnement**. Mais cela n'a pas de sens d'en parler ici entre

--

### Exemple de fonction sur les flottants

- Écrire une fonction `sum_riemann` qui, étant donné une fonction `f`
  sur les réels, deux flottants `a` et `b` et un entier `n`
  strictement positif, calcule la somme suivante &nbsp;:

$$ \frac{1}{n+1} \sum_{i=0}^{n} f(a + i \frac{b-a}{n} ) $$

```python
def sum_riemann(f, a, b, n):
    res = 0
    x, h = a, float(b - a) / n
    for i in range(n + 1):
        res = res + f(x)
        x   = x + h
    return res / (n + 1)
```
<!-- .element: class="fragment" data-fragment-index="1" -->
