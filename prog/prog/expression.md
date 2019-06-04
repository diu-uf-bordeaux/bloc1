### La trilogie

- **Valeur / Type**
  - Toute valeur à un type
  - Forme/taille de la [représentation mémoire](http://)
  - Exemple : `42` de type **int**, `"abc"` de type **str**

- **Expression**
  - Produit une valeur, possède un type
  - Exemple : `6 * 7`, `"abc"[1]`

- **Instruction** &nbsp;<span class="label">languages impératifs</span>
  - Ne produit pas de valeur (même si `None`)
  - Exemple : structures de contrôle (`if`, `for`, `return` ...)

Note:
Même si non explicite il y'a des types partout
Les règles de typage sont dépendante de la théorie utilisée derrière
mais globalement le concept est similaire
Les instructions c'est pas dans ts les langages mais le concept de forme spéciale si

--

### Un monde de valeurs
#### Littéraux

- Types simples : \
  entiers (`42`), flottants (`42.0`), booléens (`True`), \
  chaînes de caractères (`"Hello"`)

- Types structurés : \
  listes (`[]`), dictionnaires (`{:}`), t-uples (`(,)`), ensemble (`{}`)

- Fonctions (`lambda`)

> Exercice: Regarder avec `type` le resultat. Profitez en pour essayer `help`

Note:
Parler de la construction et de l'envoi de message mais botter en touche (le
premier sera vu plus tard).
On peut faire ressentir le graphe d'objet sous-jacent

--

### Opérateurs

- Purement syntaxique => un envoi de message

~~~
([1, 2*1, 1 + 2*1][2] + 3**2 * 2) * 2
~~~

- Ordre d'évaluation
- Associativité / [Précédence]

[Syntaxe]: https://docs.python.org/3/reference/expressions.html
[Précédence]: https://docs.python.org/3/reference/expressions.html#operator-precedence
