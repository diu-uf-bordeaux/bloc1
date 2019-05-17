# 1-HTML

Tous les sites web sont composés de pages HTML.

Une page HTML c'est du texte qui commence par un prologue et qui est ensuite structuré par des balises.

## Contenu d'une page HTML minimaliste

Une page HTML minimaliste contient le texte suivant :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Ma page HTML</title>
    </head>
    <body>
        Ceci est ma premiere page HTML !
    </body>
</html>
```

La première ligne est le prologue. Il précise que le reste du texte est du HTML.

Le texte contient ensuite des balises ouvrantes (`<html>` ou `<title>`), des balises fermantes (`</html>` et `</title>`.

Ces balises ouvrantes et fermantes constituent un arbre (qui est marqué ici par l'indentation du texte mais ce n'est pas obligatoire).

Notre exemple contient les balises suivantes : 
* `<html>` : Représente la racine de l'arbre HTML.
* `<head>` : Cette balise contient les informations (méta-données) de la page HTML.
* `<title>` : Cette balise permet de donner un titre à la page. Ce titre sera affiché par le navigateur dans l'onglet.
* `<body>` : Cette balise représente le contenu de la page. Ce contenu sera affiché par le navigateur.

**A l'aide de Chrome ouvrez la page index.html dans un navigateur**

## Page HTML et arbre DOM

Un navigateur web (ex. Chrome) affiche une page HTML.
 
Tous les navigateurs ont la même structure interne lorsqu'ils affichent une page HTML : c'est ce qu'on appelle le DOM (Document Object Model).

Cette structure est arborescente. Chaque balise HTML est représenté par un élément (DOM Element).

**Ouvrez les outils de développement de Chrome (appuyez sur F12) et, dans l'onglet element vous pouvez visualiser le DOM**

Un navigateur web (ex. Chrome) affiche une page HTML.

Tous les navigateurs ont la même structure interne lorsqu'ils affichent une page HTML : c'est ce qu'on appelle le 

**A l'aide d'un éditeur de code ouvrez la page index.html et modifiez la pour voir les effets de vos modifications (essayez de supprimer la balise html, et de ne pas fermer certaines balise, vous verrez que Chrome est relativement indulgent)**


## Quelques balises HTML intéressantes

### La base a

### Les balises h1, h2, h3

### Les balises ul et li

### Les balises table, th, tr, td

### Les balises div et span

