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

Le texte contient ensuite des balises ouvrantes et fermantes (`<html>` et `</html>`) ou encore (`</title>` et `</title>`.

L'imbrication des balises ouvrantes et fermantes constitue un arbre (qui est marqué ici par l'indentation du texte mais ce n'est pas obligatoire).

Chaque balise a une signification. Notre exemple contient les balises suivantes : 
* `<html>` : Représente la racine de l'arbre HTML.
* `<head>` : Cette balise contient les informations (méta-données) de la page HTML.
* `<title>` : Cette balise permet de donner un titre à la page. Ce titre sera affiché par le navigateur dans l'onglet.
* `<body>` : Cette balise représente le contenu de la page. Ce contenu sera affiché par le navigateur.


## Page HTML et arbre DOM

Un navigateur web (ex. Chrome) affiche une page HTML.
 
Tous les navigateurs ont la même structure interne lorsqu'ils affichent une page HTML : c'est ce qu'on appelle le DOM (Document Object Model).

Cette structure est arborescente. Chaque balise HTML est représenté par un élément (DOM Element).

Un navigateur web (ex. Chrome) affiche une page HTML.

Tous les navigateurs ont la même structure interne lorsqu'ils affichent une page HTML : c'est ce qu'on appelle le 

## Quelques balises HTML intéressantes

### La base a

La balise `<a href='autrePage.hml'> lien vers une autre page </a>` permet de créer un lien entre deux pages HTML.

L'utilisateur pourra alors cliquer sur ce lien et le navigateur affichera la page ciblé par l'attribut `href`.

### Les balises h1, h2, h3

Les balises `<h1></h1>`, `<h2></h2>`, `<h3></h3>`, `<h4></h4>` et `<h5></h5>` représentent des titres de section à différents niveau (1 à 5).

### Les balises ul et li
Les balises `<ul></ul>` et `<ll></li>` permettent de faire des listes d'items.

Par exemple:

```html
<ul>
    <li>item1 </li>
    <li>item2 </li>
    <li>item3 </li>
</ul>
```

### Les balises table, th, tr, td
Ces balises permettent de faire d'afficher des tableaux:

```html
<table>
    <thead>
        <tr>
            <th colspan="2">The table header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The table body</td>
            <td>with two columns</td>
        </tr>
    </tbody>
</table>
```

### Les balises div et span

Ces balises sont extrêment utiles car elles délimitent des parties de la page HTML qui pourront être identifiées par  [CSS](../2-CSS) ou par [JavaScript](../3-JS).

## Mise en pratique

**A l'aide de Chrome ouvrez la page index.html dans un navigateur**

**Ouvrez les outils de développement de Chrome (appuyez sur F12) et, dans l'onglet element vous pouvez visualiser le DOM**

**A l'aide d'un éditeur de code ouvrez la page index.html et modifiez la pour voir les effets de vos modifications (essayez de supprimer la balise html, et de ne pas fermer certaines balise, vous verrez que Chrome est relativement indulgent)**

**Avec Chrome, ouvrez la page index.html du répertoire bj et modifiez la pour changer les cartes**

**Ajoutez dans la page index.html un lien qui point vers la page bj/index.html**
