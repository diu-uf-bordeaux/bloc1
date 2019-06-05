const PORT = 80;
const express = require('express');
const app = express();
const bodyParser = require('body-parser');

const mainsDesJoueurMap = new Map();

app.use(express.static('public'));
app.use(bodyParser.json());

app.post('/nouvelle-donne',function(req, res) {
    mainsDesJoueurMap.set(req.body.nom, nouvelleMain())
    res.status(200).send({nom: req.body.nom});
});

app.get('/carte',function(req, res) {
    let main = mainsDesJoueurMap.get(req.query.nom);
    res.status(200).send({carte:nouvelleCarte(main)});
});

app.listen(PORT, function () {
    console.log(`Server is running on port ${PORT}!`)
})


function nouvelleMain() {
    let cartes = new Array();
	for (let i = 1; i < 53; i++) { 
	    cartes[i] = 0;
    }
    return cartes;
}

function nouvelleCarte(main) {
	let i = Math.floor((Math.random()*52)+1);
    while (main[i] != 0) {
        i = Math.floor((Math.random()*52)+1);
    }
    main[i] = 1;
    if (i < 10) {
        return `0${i}`;
    } else {
        return `${i}`;
    }
}