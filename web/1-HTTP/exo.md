# Mise en pratique

## Observation des requêtes HTTP

À l'aide de votre navigateur web (Chrome) et des outils de développement (onglet _Network_),  ouvrez [la page du LaBRI](http://www.labri.fr) et observez les requêtes HTTP.
En outre, vérifiez que vous faites les observations suivantes :

1. Plus de 20 requêtes sont envoyées pour afficher la page web.
2. La première requête cible la page `index.php` et retourne du HTML (ce qui donne un indice sur le type de serveur).
3. La seconde requête cible la feuille de style `labri.css`.
4. Les autres requêtes retournent des images.
5. Toutes les requêtes sont des **GET**.
6. Le serveur traite toutes les requêtes avec succès (code 200).


Ouvrez maintenant [la page Google](https://www.google.fr) et observez les requêtes HTTP.
Commencez à saisir une recherche Google et faites les observations suivantes :

1. Plus de 20 requêtes sont envoyées pour afficher la page web.
1. Une requête `search` est envoyée à chaque fois qu'on saisie une lettre.
1. Ces requêtes sont des **GET**.
1. Ces requêtes sont toutes traitées avec succès par le serveur mais celui-ci ne retourne pas de HTML (regardez la réponse).

## Serveur Statique

Nous avons développé un serveur web statique très simpliste (voir répertoire `static`).

Pour démarrer ce serveur, exécutez les lignes suivantes depuis un terminal à l'intérieur du répertoire `static` :

    npm install
    node index.js


Vous pourrez alors vérifier que votre navigateur peut charger la page web contenue dans le répertoire `public` en allant à cette URL : [http://localhost](http://localhost)

Copiez dans le répertoire `public` tous les fichiers que vous avez réalisés pour coder [l'exercice 3](../3-JS/exo.md)


## Serveur dynamique



## Serveur de web service ou de ressources REST

