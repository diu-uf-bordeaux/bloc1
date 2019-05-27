//Cette fonction sera exécutée dès que le DOM sera chargé
function initialization() {
    nouvellePartie();

    //TODO-1: ajouter 1 carte dès le début
    ajouterCarte(`./img/${nouvelleCarte()}.BMP`);

    //TODO-2: ajouter le listener sur le bouton
    addButtonListener();
}

function ajouterCarte(src) {
    let img = document.createElement('img');
    img.src = src;
    document.getElementById("mes-cartes").appendChild(img);
}

function clickOnAjouterCarte() {
    //TODO-3: ajouter une carte
    ajouterCarte(`./img/${nouvelleCarte()}.BMP`);
}

function addButtonListener() {
    let ajouterCarteButton = document.getElementById("boutton-ajout-carte");
    ajouterCarteButton.onclick = clickOnAjouterCarte;
}

//Gérer le hasard
var cartes = new Array();
function nouvellePartie() {
	for (let i = 1; i < 53; i++) { 
	    cartes[i] = 0;
	}
}
function nouvelleCarte() {
	let i = Math.floor((Math.random()*52)+1);
    while (cartes[i] != 0) {
        i = Math.floor((Math.random()*52)+1);
    }
    if (i < 10) {
        return `0${i}`;
    } else {
        return `${i}`;
    }
}




window.onload = initialization;