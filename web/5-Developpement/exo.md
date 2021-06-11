---
layout: article
title: Mise en pratique
sidebar:
  nav: web
---

Téléchargez et décompressez l'archive [developpement.zip](developpement.zip).

## Serveur de pages statiques

Nous avons codé un serveur en JavaScript qui gère uniquement les pages statiques.

Lancez ce serveur en allant dans répertoire `static` et en exécutant les deux commandes suivantes :

```javascript
  npm install
  node index.js
```

Vous devriez alors pouvoir cibler ce serveur depuis votre navigateur en allant sur l'URL : [http://localhost:3000](http://localhost:3000)

Ouvrez le fichier `index.js` à l'aide d'un éditeur de code ([VS Code](https://code.visualstudio.com) par exemple) et constatez le peu de lignes de code nécessaires grâce à l'utilisation de la bibliothèque [Express](http://expressjs.com).

Copiez / Collez les pages HTML du BlackJack dans le répertoire `public` du serveur et chargez-les avec votre navigateur.

### Accès à travers le réseau

Le serveur qui s'exécute sur votre machine est accessible à travers le réseau grâce à l'adresse IP de la machine ou à son nom.

Accèder au serveur de votre voisin en ciblant sa machine depuis votre navigateur avec l'URL : [http://nom_machine_voisin:3000](http://nom_machine_voisin:3000)

Vérifiez, à l'inverse, que votre voisin parvient bien à accèder à votre serveur. Modifiez la page `index.html` dans votre répertoire `public`, puis rafraîchissez l'affichage dans le navigateur de votre voisin.

## Serveur de pages dynamiques

Nous avons codé un serveur de page dynamique.

Lancez ce serveur en allant dans le répertoire `dynamic` et en exécutant les deux commandes suivantes:

```javascript
  npm install
  node index.js
```

Modifiez la page `index.html` afin que le formulaire envoie une requête POST vers l'URL `/cartes` avec une donnée `nom` contenant le nom saisi par le joueur.

Ajoutez une validation des données saisies dans le formulaire à l'aide du _middleware_ [express-validator](https://express-validator.github.io/docs/).