function initialization() {
    document.getElementById("cartes").style.display = 'none';
    addFormListener();
    addButtonListener();
}

function addFormListener() {
    let form = document.getElementById("saisie-nom");
    form.onsubmit = submitForm;
}

function submitForm(event) {
    event.preventDefault();
    let body = {
        nom : document.getElementById("input-nom").value
    }
    fetch('nouvelle-donne', {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: 'post',
            body: JSON.stringify(body)
        })
        .then( function(resp) {
            return resp.json();
        })
        .then ( function(data) {
            console.log(JSON.stringify(data));
            document.getElementById("nom").innerHTML = data.nom;
            document.getElementById("cartes").style.display = 'block';
            document.getElementById("saisie-nom").style.display = 'none';
        })
}

function addButtonListener() {
    let ajouterCarteButton = document.getElementById("boutton-ajout-carte");
    ajouterCarteButton.onclick = clickOnAjouterCarte;
}

function clickOnAjouterCarte() {
    fetch(`carte?nom=${document.getElementById("input-nom").value}`)
        .then(function (resp) {
            return resp.json();
        })
        .then(function(data) {
            ajouterCarte(`./img/${data.carte}.BMP`);
        })
}


function ajouterCarte(src) {
    let img = document.createElement('img');
    img.src = src;
    document.getElementById("mes-cartes").appendChild(img);
}








window.onload = initialization;