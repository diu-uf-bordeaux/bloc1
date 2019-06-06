# Mise en pratique


## Serveur de pages statiques

Nous avons codé un serveur qui est gère uniquement les pages statiques.

Lancez ce serveur en allant dans repertoire **static** et en exécutant les deux commandes suivantes :

    npm install
    
    node index.js

Vous devriez pouvoir cibler ce serveur depuis votre navigateur en allant sur l'URL : [http://localhost](http://localhost)

Copiez / Collez les pages HTML du BlackJack dans le répertoire **public** du serveur et chargez les avec votre navigateur.

Le serveur qui s'exécute sur votre machine est accessible à travers le réseau grâce à l'adresse IP de la machine. Pour déterminer cette dernière, tapez la commande suivante dans un terminal : 

    ip route get 1 | awk '{print $NF;exit}'

Échangez l'adresse IP obtenue avec votre voisin et accèder à son serveur en le ciblant depuis votre navigateur avec l'URL : [http://<adresse_IP>](http://<adresse_IP>)

Vérifiez, à l'inverse, qu'il parvient bien à accèder à votre serveur. Modifiez la page **index.html** dans votre répertoire **public**, puis rafraîchissez l'affichage dans le navigateur de votre voisin.

## Serveur de pages dynamiques

Nous avons codé un serveur de page dynamique.

Lancez ce serveur en allant dans le repertoire **dynamic** et en exécutant les deux commandes suivantes:

    npm install

    node index.js

Modifiez la page **index.html** afin que le formulaire envoie un message POST vers l'URL **/cartes** avec une donnée **nom** contenant le nom saisie par le joueur.

