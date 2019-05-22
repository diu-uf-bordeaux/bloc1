# JavaScript - Principes de Base

Le langage [JavaScript](https://fr.wikipedia.org/wiki/JavaScript) a été principalement défini pour être exécuté dans un navigateur web.

Pour autant, depuis quelques années, il a gagné en popularité et est aujourd'hui utilisé dans bien d'autres contextes.

## Interprétation(s)

JavaScript est un langage interprété. Cela veut dire qu'il est exécuté par un interpréteur sans qu'une phase de compilation soit nécessaire.
[NodeJS](https://nodejs.org/en/) est l'interpréteur populaire de JavaScript.

JavaScript est un standard ECMA : [ECMA Script](https://developer.mozilla.org/fr/docs/Web/JavaScript/Language_Resources). On comprend alors qu'il y a des différences entre le standard et les interpréteurs (c.f. [compatibilité NodeJS / ECMA ](https://node.green/)).

## Typage dynamique

En JavaScript les variables sont typées mais le typage est dynamique, c'est à dire qu'il change lors de l'exécution.

De plus, le typage est implicite et calculé par l'interpreteur. Le code source ne mentionne pas les types.

```javascript
var a;
var b;
a = 5; //a est un nombre
b = '5'; // b est une chaîne de caractère
var c = (a === b); //a===b teste l'égalité (valeur et type) de a et b, le resultat est faux. c est donc un boolean.
b = 10; //maintenant b est un nombre
c = a + b; // c vaut 15
```

## Fonctionnel (mais pas pur)

JavaScript est plutôt apparenté aux langages fonctionnels. Cela veut dire que la fonction est l'élément de premier plan. En JavaScript les fonctions structurent le code. 

Pour autant, JavaScript n'est pas un langage fonctionnel pur car les fonctions peuvent avoir des effets de bord, c'est à dire qu'elles peuvent modifier des variables qui n'apparatiennent pas à la fonction.

Par exemple, le code suivant défini une fonction qui modifie une variable qui ne lui appartient pas.

```javascript
var a;

function f() {
    a = 5;
}

f();
```

## Objet (enfin plutôt dictionnaire)

JavaScript propose un concept d'objet qui est un dictionnaire : ensemble de couples (nom, valeur).

Le code définit la variable **johnSnow** qui est un objet. Cet objet possède trois propriétés : first, last, isAlive.
On peut accéder aux propriétés des objets (lecture et écriture).

```javascript
var johnSnow = {
    first : 'John',
    last : 'Snow',
    isAlive : undefined
}

johnSnow.isAlive = true;
```

## Objet et fonction

Un objet peut définir une fonction. Par exemple le code suivant défini l'objet johnSnow dont l'une de ses propriétés est une fonction.



```javascript
var johnSnow = {
    first : 'John',
    last : 'Snow',
    isAlive : undefined,
    resurrect : f() {
        this.isAlive = true;
    }

}

johnSnow.resurrect();
```

Lorsqu'un objet défini une fonction, il est possible d'appeler la fonction à partir de l'objet. Ainsi fait, le mot clé **this** dans la fonction référence l'objet qui défini la fonction.


## Asynchrone et événementiel

Un interpréteur JavaScript est mono-thread, c'est à dire qu'une seule instruction est exécuté à la fois.

De fait, pour maximiser les interactions, JavaScript supporte l'asynchronisme. Les fonctions asynchrones peuvent voir leur exécution temporairement suspendue.

Plusieurs mécanismes servent à gérer l'asynchronimse dans le code source. Le plus vieux étant le concept de callBack. Une callBack est une fonction qui sera appelée lorsque l'exécution d'une fonction asynchrone sera terminée (on passe alors la callBack comme paramètre de la fonction asynchrone).

Le code suivant illustre ce principe à l'aide de la fonction **setTimeout** qui est asynchrone. Cette fonction suspend son exécution pendant un laps de temps puis exécute la callBack passée en paramètre (ici la fonction **maCallBack**)

```javascript
function maCallBack() {
    console.log('fin du timer');
}
setTimeout(maCallBack, 2000);
```

D'autres mécanismes facilitant l'écriture de code asynchrone ont été proposés : Promise et async/await.

Ce mécanisme d'asynchronisme est beaucoup utilisé pour gérer les évennements. L'idée est d'enregistrer des callBack sur des événements. Celles-ci seront appelées lors que les événements 