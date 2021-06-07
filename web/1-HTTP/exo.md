---
layout: article
title: Mise en pratique HTTP
sidebar:
  nav: web
---

## Observation des requêtes HTTP

À l'aide de votre navigateur web (Chrome ou Firefox) et des outils de développement (onglet _Network_),  ouvrez [la page du CREMI](https://www.emi.u-bordeaux.fr/) et observez les requêtes HTTP.
En outre, vérifiez que vous faites les observations suivantes :

1. Un vingtaine de requêtes sont envoyées pour afficher la page web.
2. La première requête cible la page racine et retourne du HTML (ce qui donne un indice sur le type de serveur).
3. La seconde requête cible la feuille de style `main.css`.
4. Les autres requêtes retournent des scripts Javascript et des images.
5. Toutes les requêtes sont des **GET**.
6. Le serveur traite toutes les requêtes avec succès (code 200).
7. Certaines requêtes sont à destination d'uu autre serveur (https://fonts.googleapis.com)


Ouvrez maintenant [la page Google](https://www.google.fr) et observez les requêtes HTTP.
Commencez à saisir une recherche Google et faites les observations suivantes :

1. Plus de 20 requêtes sont envoyées pour afficher la page web.
1. Une requête `search` est envoyée à chaque fois qu'on saisie une lettre.
1. Ces requêtes sont des **GET**.
1. Ces requêtes sont toutes traitées avec succès par le serveur mais celui-ci ne retourne pas de HTML (regardez la réponse).

