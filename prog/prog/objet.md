### Un monde d'objets

- En Python, toute valeur est un **objet**, auquel on envoie des
  **messages**.

`object.method(params)`

- Exemples : insérer ici

> Regarder que peut faire un objet : `dir(uneExpression)`

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

  - initialisation de l'instance :
      appel au constructeur `__init__`

- Exemples : `list()`, `str()`, `date(1789, 7, 14)`
