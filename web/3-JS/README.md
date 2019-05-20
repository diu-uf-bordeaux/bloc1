# 3-JS

## HTML et JS

Tous les navigateurs embarquent un moteur [JavaScript](./JavaScript.md) qui permet d'exécuter du code sur le DOM.

L'objectif est de rendre la page dynamique, qu'elle réponde aux interactions de l'utilisateur.

Le code JavaScript s'exécute sur le DOM, mais pour cela il faut le charger dans le navigateur.

Pour ce faire, il est possible d'ajouter le code JavaScript dans la page HTML.

```html
<script>
window.addEventListener('load', function () {
  console.log('Cette fonction est exécutée une fois quand la page est chargée.');
});
</script>
```

ou bien de mettre le code JavaScript dans un fichier (.js) et de pointer ce fichier depuis le HTML.

```html
<script src="./script.js"></script>
```

avec script.js :

```javascript
console.log('Cette fonction est exécutée une fois quand la page est chargée.');
```

## DOM Element

Grâce à JavaScript il est possible de manipuler dynamiquement les éléments du DOM.

Les éléments DOM sont des objets JavaScript qui proposent une [API](https://www.w3schools.com/jsref/dom_obj_all.asp).

L'élément racine du DOM est le **document** qui propose une [API plus riche](https://www.w3schools.com/jsref/dom_obj_document.asp).

En utilisant la console dans les outils de développement de Chrome, il est possible d'accéder au **document** juste.
On peut alors le manipuler dynamiquement et observer le résultat dans le navigateur.

Par exemple, si on écrit ``document.body.innerHTML = "VIDE";`` dans la console, 


On peut alors retrouver l'intégralité du DOM.





Jouer avec la console Chrome pour accéder aux objets DOM et les modifier

## DOM Event
Présenter le concept de DOM Event

Ajouter un listener et lui faire ajouter qqc 
