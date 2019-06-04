### La trilogie

- **Type**
  - Toute valeur à un type
  - Forme/taille de la case mémoire\
    (cf. Représentation des données)

- **Expression**
  - Évaluable (produit une valeur) => type

- **Instruction**
  - (Pour les languages impératifs) <!-- .element class="small" -->
  - Exécutable => pas de type (même si `None`)
  - Formes spéciales

Note:
Même si non explicite il y'a des types partout
Les règles de typage sont dépendante de la théorie utilisée derrière
mais globalement le concept est similaire
Les instructions c'est pas dans ts les langages mais le concept de forme spéciale si

--

### Un monde (d')Objet
#### Littéraux

- Types simples: \
  entiers (`42`), flottants (`42.0`), booléens (`True`), caractères (`'a'`)
- Types structurés : \
  chaînes de caractères (`"Hello"`),listes (`[]`), dictionnaires (`{}`), t-uples (`(,)`)
- Fonctions (`fact`, notez l'absence de parenthèse)

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
