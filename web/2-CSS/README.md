# 2-CSS

Si les balises HTML permettent de structurer une page HTML (structuration du fond), c'est le langage CSS qui permet d'affiner la forme visuelle d'une page.

## CSS et HTML

CSS et HTML sont deux langages différents mais complémentaires. 

CSS défini des styles (essentiellement graphiques) qui ciblent les balises HTML et leurs contenus.

Il est possible d'ajouter les styles CSS directement dans une page HTML.

```html
<head>
    <style>
        body {background-color: powderblue;}
        h1   {color: blue;}
        p    {color: red;}
    </style>
</head>
```

ou de les définir dans un fichier (.css) et de pointer ce fichier dans la page HTML

```html
<head>
  <link rel="stylesheet" href="styles.css"/>
</head>
```

avec le fichier styles.css:
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

## propriétées graphiques de base CSS

CSS défini un ensemble important de propriétés qui permettent de configurer le style (essentiellement graphique d'une page HTML.

Par exemple la propriétés `background-color` défini la couleur de fond. Un style définira alor la couleur voulue : `orange`, `blue`, `#DA70D6` ou même `rgb(255,0,255)`.

Le langage CSS défini un grand nombre de propriétée et précise les valeurs possibles pour chacune d'entre elles.


## sélecteur CSS

Un style CSS s'attache à certains éléments d'une page HTML.

Lorsqu'on défini un style CSS, il faut alors préciser à quels éléments il s'attache (on parle de selecteur).

Cela peut se faire de trois façons.

### Un style attaché à une balise
Un style peut s'attacher à tous les éléments d'une certaine balise HTML

Par exemple ce style : 
```css
h1 {
  color: blue;
}
```
s'attache à tous les éléments `<h1></h1>` où qu'ils soient dans la page.

### Un style attaché à une balise
Un style peut s'attacher à une classe.

Par exemple ce style :
```css
.beau {
    coloe: blue;
}
```

Défini la classe `beau` et précise qu'il s'attache à tous les éléments qui ont cette classe.

Ajouter une classe à un élément se fait dans la balise `<h1 class=beau> Mon beau titre </h1>`

### Un style attaché à un identifiant
Un style peut s'attacher à un identifiant.

Par exemple ce style :
```css
#principal {
    coloe: blue;
}
```

s'attache à l'élément dont l'identifiant est `principal`.

Préciser l'identifiant d'un élément se fait dans la balise `<h1 id='principal'> Mon beau titre </h1>`

### Et encore

CSS propose aussi de préciser des relations entre les balises afin d'être plus précis. 

La [norme CSS](https://www.w3schools.com/cssref/css_selectors.asp) précise toutes les constructions possibles, et surtout expliquer les priorités d'application des styles (quoi faire quand deux styles différents s'appliquent sur un même éléments ?)

## pagination

Lors de l'affichache d'une page HML à chaque élément est associé une boîte pour sa visualisation. La taille de la boite dépend de l'élément et de son contenu.

CSS propose de multiples propriétés pour changer le style des boites dans lesquels sont affichés les éléments. C'est ce qu'on appelle le [padding](https://developer.mozilla.org/fr/docs/Web/CSS/padding)

Les boite qui ne sont pas imbriquée les unes dans les autres sont affichées comme du texte au kilomètre : les unes derrières les autres, comme dans un flot.

Pour autant CSS propose différentes propriétés pour changer la façon dont les boites sont affichées, c'est ce qu'on appelle la [position des boîtes](https://www.w3schools.com/css/css_positioning.asp)

Pour faciliter la dispostion des éléments dans une page HTML, plusieurs projets proposent des styles CSS prêt à utiliser. Ils proposent différents style prêt à emploi pour positionner des éléments dans une grille et faciliter le déplacement des éléments quand la taille de la fenêtre change. L'un des plus connu est [bootstrap](https://getbootstrap.com/).

## Et bien plus encore

CSS offre de nombreuses propriétés qui permettent de rendre les pages web très dynamique.

Il est par exemple possible d'ajouter des [animations](https://developer.mozilla.org/fr/docs/Web/CSS/Animations_CSS/Utiliser_les_animations_CSS) pour faire apparaître ou disparaitre des éléments

## Mise en pratique

**changez le style CSS de l'exemple black-jack pour faire en sorte que la couleur de fond ne soit plus en noir**

**ajoutez un style pour faire en sorte que les montants du joueurs et de la banque (balise span) soit dans une police plus grosse**

**utilisez les outils de développement de Chrome pour changer observer les styles mis en oeuvre lors de l'affichage de la page, et changez les dynamiquement (par exemple en ajoutant un style qui modifie le padding)**

**Ouvrez une page Youtube ou Facebook changez là pour modifier son style et son contenu** 