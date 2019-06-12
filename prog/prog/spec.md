### Spécification

- Une **spécification** pour un programme est un ensemble de
  propriétés qu'il est censé vérifier.

- Il s'agit d'un outil d'aide à la **vérification** de programme.

- Idée : assurer la **correction** (le résultat est-il juste ?) et \
  la **fiabilité** (le calcul se fait-il sans erreurs ?) du code.

<br/>

- Techniques possibles&nbsp;: preuve formelle, vérification de
  modèles, analyse statique, test, monitoring ...

Note:
Fiabilité == le code n'explose pas
Correction == le code fait ce qu'il prétend faire

--

### Spécification : logique

- Une spécification peut s'exprimer sous la forme d'un ensemble de
  règles **logiques**.

- Principe (dérivé de la logique de Hoare)&nbsp;: préciser, pour toute
  fonction ou programme&nbsp;:

    - une **précondition** vérifiée avant l'exécution,
    - une **postcondition** vérifiée au retour de l'exécution,
    - des **invariants** préservés par l'exécution.

- Ces spécifications se composent lorsque l'on compose les fonctions /
  programmes.

--

### Spécification : exemple

```python
def join(lst, sep):
    """Concatène les éléments d'une liste avec un séparateur"""
    result = lst.copy().pop(0)
    for l in lst:
        result = result + sep + l
    return result
```

|||
|-|-|
| Précondition  | &bullet; `lst` est une liste de chaînes de caractères, <br/> &bullet; `sep` est une simple chaîne. |
| Postcondition | &bullet; le résultat est la concaténation des valeurs <br/> de `lst` séparées par `sep`, <br/> &bullet; `lst` a perdu son premier élément. |
| Invariants    | &bullet; `sep` n'est pas modifié |
|||


--

### Spécification : types

- Les **types** constituent une technique de spécification vérifiable
  de manière automatique par une analyse du code.

- Principe&nbsp;:

  - annoter les programmes en explicitant les types
    utilisés (paramètres de fonctions, retours, variables ...)

  - vérifier que la composition des appels de fonctions réalisés dans
    le programme est cohérente.

- Exemples d'erreurs&nbsp;:

```python
{ "x": 1 }.reverse()  # error : 'dict' object has no attribute 'reverse'
1 + "deux"            # error : unsupported types for +: 'int' and 'str'

```


--

### Vérification : types

- Dans des langages aux systèmes de types plus perfectionnés, les
  types permettent aussi de :

    - prévenir des erreurs avant l'exécution du code;

    - optimiser du code suivant sa représentation.

- Néanmoins, ils peuvent être un frein au développement en
  contraignant les possibilités des programmeurs.

    Ainsi, `join` s'applique aussi à des listes de nombres.


--

### Vérification : tests

- Le **test** est une technique de vérification consistant à exécuter
  le code pour en vérifier le comportement.

- Extrêmement simple à appliquer (le faire systématiquement).

- Un **cas de test** est une spécification des entrées et des
  résultats attendus lors de l'exécution d'un code.

- Ex.&nbsp;: `join(["a", "b"], " and ")` renvoie `"a and b"`

- Principe&nbsp;: exécuter le code sur en ensemble de cas de tests
  assurant une bonne **couverture du code**.

- Faiblesse&nbsp;: les tests ne vérifient pas toutes les exécutions.

"Testing shows the presence, not the absence of bugs"

--

### Vérification : exemples de tests

- Pour la fonction `join`, un ensemble de cas de tests possible&nbsp;:

<br/>

| Entrée | Retour | Explication
|-|-|-|
|`join([], "")` | `""` | longueur nulle |
|`join([], ",")` | `""` | longueur nulle |
|`join(["a"], ",")` | `"a"` | longueur 1 |
|`join(["a", "b"], "")` | `"ab"` | longueur > 1 |
|`join(["a", "b"], ",")` | `"a,b"` | longueur > 1 |
|||

- C'est l'occasion de voir qu'elle ne gère pas les tableaux vides.
