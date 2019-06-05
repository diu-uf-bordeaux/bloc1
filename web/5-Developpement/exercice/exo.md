# Mise en pratique


## Serveur de pages statiques

Nous avons codé un serveur qui est gère uniquement les pages statiques.

Lancez ce serveur en allant dans repertoire **static** et en executant les deux commandes suivantes :

    npm install
    
    node index.js

Vous devriez pouvoir cibler ce serveur depuis votre navigateur en allant sur l'URL : [http://localhost](http://localhost)

Copiez / Collez les pages HTML du BlackJacj dans le répertoire **public** du serveur et chargez les avec votre navigateur.

## Serveur de pages dynamiques

Nous avons codé un serveur de page dynamique.

Lancez ce serveur en allant dans le repertoire **dynamic** et en executant les deux commandes suivantes:

    npm install

    node index.js

Modifiez la page **index.html** afin que le formulaire envoie un message POST vers l'URL **/cartes** avec une donnée **nom** contenant le nom saisie par le joueur.

