# 3-JS

## HTML et JS

Tous les navigateurs embarque un moteur JavaScript qui permet d'exécuter du code sur le DOM.

L'objectif est de rendre la page dynamique, qu'elle réponde aux interaction de l'utilisateur.

Le code JavaScript s'exécute sur le DOM, mais pour cela il faut le charger dans le navigateur.

Pour ce faire, il est possible d'ajouter le code JavaScript dans la page HTML.

```html
<script>
window.addEventListener('load', function () {
  console.log('Cette fonction est exécutée une fois quand la page est chargée.');
});
</script>
```

ou bien de mettre le code JavaScript dans un fichier (.js) et de pointer ce fichier.

```html
<script src="./script.js"></script>
```

avec script.js :

```javascript
console.log('Cette fonction est exécutée une fois quand la page est chargée.');
```
## DOM Element
Présenter le concept d'objet JS DOM Element.

Jouer avec la console Chrome pour accéder aux objets DOM et les modifier

## DOM Event
Présenter le concept de DOM Event

Ajouter un listener et lui faire ajouter qqc 
