# 3 - CSS

Si les balises HTML permettent de structurer une page HTML (structuration du fond), c'est le langage CSS qui permet d'affiner la forme visuelle d'une page.

## CSS et HTML

CSS et HTML sont deux langages différents mais complémentaires. 

CSS définit des styles (essentiellement graphiques) qui ciblent les balises HTML et leur contenu.

Il est possible d'ajouter les styles CSS directement dans une page HTML lorsqu'une page HTML à un style unique :

```html
<head>
    <style>
        body {background-color: powderblue;}
        h1   {color: blue;}
        p    {color: red;}
    </style>
</head>
```

ou de les définir dans un fichier externe (.css) et de pointer ce fichier dans la page HTML :

```html
<head>
  <link rel="stylesheet" href="styles.css"/>
</head>
```

avec le fichier `styles.css` :
```css
body {
  background-color: powderblue;
}
h1 {
  color: blue;
}
p {
  color: red;
}
```

## Propriétés graphiques de base CSS

CSS définit un ensemble important de propriétés qui permettent de configurer le style (essentiellement graphique) d'une page HTML.

Par exemple, la propriétés `background-color` définit la couleur de fond de la page. Un style définira alors la couleur voulue à l'aide d'un mot clé (`orange`, `blue`, etc.), d'un code hexadécimal (`#DA70D6`), ou même de valeurs RGB (`rgb(255,0,255)`).

Le langage CSS définit un grand nombre de propriétés et précise les valeurs possibles pour chacune d'entre elles.


## Sélecteur CSS

Un style CSS s'attache à certains éléments d'une page HTML. Lorsqu'on définit un style CSS, il faut donc préciser à quels éléments il s'attache (on parle de sélecteur).

Cela peut s'effectuer de trois façons.

### Un style attaché à une balise
Un style peut s'attacher à tous les éléments d'une certaine balise HTML.

Par exemple ce style : 
```css
h1 {
  color: blue;
}
```
s'attache à tous les éléments `<h1></h1>` où qu'ils soient dans la page HTML.

### Un style attaché à une classe
Un style peut s'attacher à une classe.

Par exemple ce style :
```css
.beau {
    color: blue;
}
```

définit la classe `beau`. Il s'appliquera à tous les éléments qui possèdent cette classe.

Une classe est donnée à un élément dans sa balise HTML par l'attribut `class` : `<h1 class="beau"> Mon beau titre </h1>`

Un élément peut posséder plusieurs classes, le nom de chacune d'elles étant séparé par un espace : `<h1 class="beau grand"> Mon beau titre </h1>`

### Un style attaché à un identifiant
Un style peut s'attacher à un identifiant.

Par exemple ce style :
```css
#principal {
    color: blue;
}
```

s'attache à l'élément dont l'identifiant est `principal`.

Préciser l'identifiant d'un élément se fait dans sa balise HTML par l'attribut `id` : `<h1 id='principal'> Mon beau titre </h1>`

Un élément possède un unique identifiant.

### Et encore...

CSS propose aussi de préciser des relations entre les balises afin d'être plus précis. 

La [norme CSS](https://www.w3schools.com/cssref/css_selectors.asp) précise toutes les constructions possibles, et surtout explique les priorités d'application des styles (quoi faire quand deux styles différents s'appliquent sur un même éléments ?)

## Pagination

Lors de l'affichage d'une page HML, une boîte est associée à chaque élément pour sa visualisation. La taille de cette boîte dépend de l'élément et de son contenu.

CSS propose de multiples propriétés pour changer le style des boîtes dans lesquels sont affichés les éléments. On peut notamment contrôler ses marges intérieurs ([padding](https://developer.mozilla.org/fr/docs/Web/CSS/padding)) et extérieurs ([margin](https://developer.mozilla.org/fr/docs/Web/CSS/margin)) et son encadrement ([border](https://developer.mozilla.org/fr/docs/Web/CSS/border)).

Les boîte qui ne sont pas imbriquée les unes dans les autres sont affichées comme du texte au kilomètre : les unes derrières les autres, comme dans un flot.

Pour autant CSS propose différentes propriétés pour changer la façon dont les boîtes sont affichées, c'est ce qu'on appelle la [position des boîtes](https://www.w3schools.com/css/css_positioning.asp).

Pour faciliter la disposition des éléments dans une page HTML, plusieurs projets proposent des styles CSS directement utilisables. Ils proposent différents styles pour positionner des éléments dans une grille et faciliter le déplacement des éléments quand la taille de la fenêtre change. L'un des plus connu est [bootstrap](https://getbootstrap.com/).

## Et bien plus encore

CSS offre de nombreuses propriétés qui permettent de rendre les pages web très dynamiques.

Il est par exemple possible d'ajouter des [animations](https://developer.mozilla.org/fr/docs/Web/CSS/Animations_CSS/Utiliser_les_animations_CSS) pour faire apparaître ou disparaître des éléments.

## Mise en pratique

Continuez vers [la mise en pratique](./exo.md) 
