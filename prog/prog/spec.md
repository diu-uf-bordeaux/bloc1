### Spécification

- La spécification est un outil d'aide à la vérification de programme.

- Idée : assurer la **fiabilité** et la **correction** du code.

Note:
Fiabilité == le code n'explose pas
Correction == le code fait ce qu'il prétend faire

--

### Spécification : logique

- Logique / Propriétés

- Précondition, Postcondition, Invariant

--

### Spécification : types

- Les types constituent une technique de spécification


--

### Vérification : types


- Mesure de fiabilité : vérifications de la composition des fonctions

- Dans des langages aux systèmes de types plus perfectionnés, les
  types permettent aussi de :

    - prévenir des erreurs avant l'exécution du code;

    - optimiser du code suivant sa représentation.

- Néanmoins, ils peuvent être un frein au développement en
  contraignant les possibilités des programmeurs.

    Ainsi, `join` s'applique aussi à des listes de nombres.


--

### Vérification : tests

- Le test est une technique de vérification.

- Mesure de fiabilité : couverture de code
