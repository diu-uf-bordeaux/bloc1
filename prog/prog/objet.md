### Un monde d'objets

- En Python, toute valeur est un **objet**, auquel on envoie des
  **messages**.

`object.method(params)`

- Exemples : `"abc"` est un objet de type **str** et répond à :

    - isdigit : `"abc".isdigit()`
    - replace : `"abc".replace("1","4")`


> Lister les messages auxquels répond un objet : `dir(expression)`

--

### Objet : envoi de message

- Lorsqu'on envoie un message à un objet **o**, on appelle une fonction
  dépendante du type de l'objet en ajoutant **o** comme premier paramètre.

    - Sans paramètres : `"CALM DOWN".lower()`

    - Avec paramètres : `" and ".join(["a", "b"])`


- Ce premier paramètre est appelé **receveur** et nommé `self`.

--

### Objet : instanciation

- La création d'un objet s'appelle une **instanciation**.

- Se découpe en deux parties :

  - allocation : préparation de la mémoire

  - initialisation : appel au constructeur `__init__`

- Exemples : `list()`, `int("10",2)`, `date(1789, 7, 14)`

- A la fin de la vie d'un objet, il est détruit avec `__del__`.


Note:
Aussi `str()` pour la chaîne vide. Attention, la plupart des
constructeurs sont des constructeurs de copie, et donc donnent une
impression bizarre de ne rien faire.
