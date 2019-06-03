# 1 - HTTP

Les fichiers qui composent un site web sont stockés sur un serveur : **le serveur web**

Souvent ces fichiers n'existent pas réellement et sont construits dynamiquement par le serveur web.

Qu'ils soient générés ou construits, ils sont envoyés par le serveur web lorsque le navigateur web en fait la requête.

C'est le [protocol HTTP](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol) qui définit la façon dont sont réalisés les échanges web sur internet.

HTTP date de 1990 et la version 2.0 est sortie en 2015.

HTTP est un protocole **question / réponse** : le client (le navigateur web) pose une question et le serveur (serveur web) y répond.

## La question

Pour poser une question, le client doit connaître l'adresse IP sur serveur et lui envoyer un message qui est constitué ainsi :
* Ligne de commande (Commande, URL, Version de protocole)
* En-tête de requête
* [Ligne vide]
* Corps de requête

La ligne de commande précise :
1. le **verbe HTTP**,
2. l'URL cible,
3. la version du protocole.

Le **verbe HTTP** précise l'intention du client, les principaux verbes sont les suivants :
* `GET` : le client veut obtenir une ressource (lire une page web),
* `POST` : le client veut ajouter une information concernant une ressource (poster un formulaire).

Mais il en existe bien d'autres : 
* `PUT` : le client veut ajouter une ressource (déposer un fichier),
* `DELETE` : le client veut supprimer une ressource (cette commande est souvent interdite),
* `PATCH` : le client veut modifier une ressource existante.
  
L'en-tête de la commande est composée de plusieurs champs (clé / valeur) tels que :
* `host` : le nom du site web, ce qui est nécessaire quand le serveur web héberge plusieurs sites web (ce qui n'est pas rare),
* `User-Agent` : le nom du navigateur web (ce qui permet d'envoyer du contenu adapté au navigateur)
* `Referer` : l'URL d'où vient le client,
* `Content-Type` : le [type MIME](https://fr.wikipedia.org/wiki/Type_de_médias) de la ressource contenue dans le message ,
* `Content-Length` : la taille de la ressource contenue dans le message.

## La réponse

La réponse est envoyée par le serveur vers le client et est constituée ainsi :
* La ligne de statut (Version HTTP, Code, message explicatif)
* En-tête de la réponse
* [Ligne vide]
* Corps de la réponse

HTTP défini plusieurs [codes pour la réponse](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) dont le fameux code **404** qui signifie que la ressource ciblée n'a pas été trouvée :
* 1xx : la requête est en cours de traitement.
* 2xx : la requête est traitée : succès (200), créée (201), etc.
* 3xx : la requête a été transférée vers un autre serveur : (301) déplacée définitivement sur un autre serveur, (304) pas modifiée donc le cache est à jours, etc.
* 4xx : il y a une erreur qui vient du client : (401) pas autorisé, (403) interdit, (404) pas trouvé, etc.
* 5xx : il y a une erreur qui vient du serveur : (501) pas implanté, (503) service down, etc.

## Mise en pratique

Continuez vers [la mise en pratique](./exo.md).
