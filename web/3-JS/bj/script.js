//Cette fonction sera exécutée dès que le DOM sera chargé
function initialization() {
    //TODO-1: ajouter 1 carte dès le début

    //TODO-2: ajouter le listener sur le bouton
}

function ajouterCarte(src) {
    let img = document.createElement('img');
    img.src = src;
    document.getElementById("mes-cartes").appendChild(img)
}

function clickOnAjouterCarte() {
    alert('click ! il faudrait ajouter une carte ');

    //TODO-3: ajouter une carte
}

function addButtonListerner(event) {
    let ajouterCarteButton = document.getElementById("boutton-ajout-carte");
    ajouterCarteButton.onclick = clickOnAjouterCarte;
}

window.onload = initialization;