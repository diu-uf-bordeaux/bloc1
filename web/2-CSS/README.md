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


## selecteur CSS

Un style CSS s'attache à certains éléments d'une page HTML.

Lorsqu'on défini un style CSS, il faut alors préciser à quels éléments il s'attache.

Cela peut se faire de trois façon.

### Un style attaché à une balise
Un style peut s'attacher à tous les éléments d'une certaine balise HTML

Par exemple ce style : 
```css
h1 {
  color: blue;
}
```
s'attache à tous les éléments `<h1></h1>`

### Un style attaché à une balise
Un style peut s'attacher à une classe.

Par exemple ce style :
```css
.beau {
    coloe: blue;
}
```

s'attache à tous les éléments dont la classe est `beau`.

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

## Et bien plus encore