# Mise en pratique

## Observation des requêtes HTTP

A l'aide de votre navigateur web (Chrome) et des outils de développement,  ouvrez [la page du LaBRI](http://www.labri.fr) et observez les requêtes HTTP.
En outre, vérifiez que vous faites les observations suivantes :

1. Plus de 20 requêtes sont envoyées pour afficher la page web 
2. La première requête cible la page index.php (ce qui donne un indice sur le type de serveur)
3. Seule la première requête retourne du HTML, les autres retournent des images
4. Toutes les requêtes sont des GET 
5. Le serveur traite toutes les requêtes avec succès (code 200)


Ouvrez maintenant [la page google](https://www.google.fr) et observez les requêtes HTTP.
Commencez à saisir une recherche google et faites les observations suivantes :

1. Plus de 20 requêtes sont envoyées pour afficher la page web
1. Une requête 'search' est envoyée à chaque fois qu'on saisie une lettre 
1. Ces requêtes sont des GET
1. Ces requêtes sont toutes traitées avec succès par le serveur mais celui-ci ne retourne pas de HTML (regardez la réponse)

## Serveur Statique



## Serveur dynamique



## Serveur de web service ou de ressources REST

