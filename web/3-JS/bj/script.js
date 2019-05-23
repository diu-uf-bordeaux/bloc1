clickAjoutCarte(src) {
    let img = document.createElement('img');
    img.src = src;
    document.getElementById("mes-cartes").appendChild(img)
}

document.getElementById("ajout-carte").onclick(clickAjoutCarte);