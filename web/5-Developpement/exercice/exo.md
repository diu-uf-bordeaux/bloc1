# Mise en pratique


## Serveur de pages statiques

Nous avons codé un serveur qui est gère uniquement les pages statiques.

Lancez ce serveur en allant dans repertoire **static** et en executant les deux commandes suivantes :

    npm install
    
    node index.js

Vous devriez pouvoir cibler ce serveur depuis votre navigateur en allant sur l'URL : [http://localhost](http://localhost)

Vous pouvez changer les pages HTML qui se trouve dans le répertoire **public** du serveur et les charger avec votre navigateur.

## Serveur de pages dynamiques

Nous avons codé un serveur de page dynamique.

Lancez ce serveur en allant dans le repertoire **dynamic** et en executant les deux commandes suivantes:

    npm install

    node index.js

Modifiez la page **index.html** et le script **script.js** afin que le formulaire envoie un message POST vers l'URL **/cartes** avec une donnée **nom** contenant le nom du joueur.

