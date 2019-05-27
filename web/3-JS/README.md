# 3-JS

## HTML et JS

Tous les navigateurs web peuvent exécuter du code [JavaScript](./JavaScript.md) qui permet d'interagir avec le DOM.

L'objectif est de rendre la page dynamique, afin qu'elle réponde aux interactions de l'utilisateur.

Le code JavaScript s'exécute sur le DOM, mais pour cela il faut le charger dans le navigateur.

Pour ce faire, il est possible d'ajouter le code JavaScript dans la page HTML à l'intérieur d'une balise :

```html
<script>
window.addEventListener('load', function () {
  console.log('Cette fonction est exécutée une fois quand la page est chargée.');
});
</script>
```

ou bien de mettre le code JavaScript dans un fichier externe (.js) et de pointer ce fichier depuis le HTML :

```html
<script src="./script.js"></script>
```

avec `script.js` :

```javascript
console.log('Cette fonction est exécutée une fois quand la page est chargée.');
```
Notons cependant que le code JavaScript sera exécuté dès que le navigateur chargera le script (ou peu de temps après). Il se peut que le code soit exécuté avant que le navigateur n'ait chargé toute la page. Si on veut que toute la page soit chargée avant d'exécuter le code, il faut alors exploiter les [événements DOM](#DOM-Event).


## DOM Element

Grâce à JavaScript il est possible de manipuler dynamiquement les éléments du DOM.

Les éléments DOM sont des objets JavaScript qui proposent une [API](https://www.w3schools.com/jsref/dom_obj_all.asp).

L'élément racine du DOM est le **document** qui propose une [API plus riche](https://www.w3schools.com/jsref/dom_obj_document.asp).

En utilisant la console dans les outils de développement de Chrome, il est possible d'accéder au **document**.
On peut alors le manipuler dynamiquement et observer le résultat dans le navigateur.

Par exemple, si on écrit ``document.body.innerHTML = "VIDE";`` dans la console, le _body_ de la page web sera dynamiquement modifié et contiendra la chaîne de caractère : "VIDE".

L'API des éléments DOM offre de nombreuses opérations pour parcourir l'arbre DOM et pour effectuer des modifications. Le code suivant retrouve l'élement HTML dont l'id est `"mondId"` et ajoute une balise `<img>` contenant l'image "02.BMP".

```javascript
var target = document.getElementById("monId");
var img= document.createElement('img');
img.src= './img/02.BMP';
target.appendChild(img);
```

## DOM Event

Le DOM émet des événements (DOM Event) lorsque ses éléments (DOM Element) subissent des interactions.

Par exemple, un évènement de type `onClick` est émis à chaque fois que l'utilisateur clique sur l'élément.

Grâce à JavaScript, on peut ajouter des traitements (fonctions _callbacks_) qui seront exécutés lorsqu'un événement sera émis.
Le code suivant ajoute par exemple la carte "01.BMP" dans l'élément d'id `"mes-cartes"` à chaque fois que l'on clique sur le bouton dont l'id est `"ajout-carte"`.

```javascript
clickAjoutCarte() {
    let img = document.createElement('img');
    img.src = './img/01.BMP';
    document.getElementById("mes-cartes").appendChild(img)
}

document.getElementById("ajout-carte").onclick(clickAjoutCarte);
```

### Glisser-Déposer (_Drag and Drop_)

Depuis la version 5 d'HTML, tout élément peut devenir déplaçable en mettant son attribut `draggable` à `true`. 

Il est ensuite nécessaire de spécifier trois _callbacks_ pour trois évènements différents :

* `ondragstart` : émis lorsque l'utilisateur clique sur l'élément à déplacer ; la _callback_ associée spécifie la donnée à déplacer en appelant la fonction `dataTransfer.setData()`, typiquement l'id de l'élément à déplacer.
* `ondragover` : émis lorsque l'élément déplacé survole un autre éléments ; pour autoriser le dépôt (interdit par défaut), la _callback_ associée appelle la fonction `event.preventDefault()`.
* `ondrop` : émis lorsque l'élément déplacé est déposé sur un autre élément ; la _callback_ associée utilise la fonction `dataTransfer.getData()` pour récupérer l'id de l'élément déplacé et modifie effectivement le DOM.

Un exemple minimal est présenté sur [cette page](https://www.w3schools.com/html/html5_draganddrop.asp).


## Mise en pratique

Continuez vers [la mise en pratique](./exo.md) 
