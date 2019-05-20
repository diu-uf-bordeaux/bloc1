var money_player = 100;
var money_bank = 100;
var cartes = new Array();


nouvellePartie = function() {
	for (i = 1; i < 53; i++) { 
	    cartes[i] = 0;
	}
};

afficheMoney = function () {
	document.getElementById("money_player").innerHTML=money_player;
	document.getElementById("money_bank").innerHTML=money_bank;
};

initPlay = function() {
	nouvellePartie();
	afficheMoney();
	document.getElementById('nouvelleCarte').onclick = nouvelleCarteJoueur;
	nouvelleCarteBank();
	document.getElementById('niveau_joueur').innerHTML = 0;
}

nouvelleCarte = function () {
	i = Math.floor((Math.random()*52)+1);
	while (cartes[i] != 0) i = Math.floor((Math.random()*52)+1);
	return i;
}

nouvelleCarteJoueur = function() {
	i = nouvelleCarte();
	cartes[i]=1;
	if (i<10) src = "img/0"+ i +".BMP";
	else src = "img/"+ i +".BMP";
	document.getElementById('player_cards').appendChild(img_create(src));
	document.getElementById('niveau_joueur').innerHTML = niveau(1,false);
};

nouvelleCarteBank = function() {
	i = nouvelleCarte();
	cartes[i]=2;
	if (i<10) src = "img/0"+ i +".BMP";
	else src = "img/"+ i +".BMP";
	document.getElementById('bank_cards').appendChild(img_create(src));	
};

niveau = function(id , as) {
	var niveau=0;
	for (i=1 ; i < 53 ; i++) {
		if (cartes[i] == id) {
			cart = i % 13 ;
			if (cart == 1) {
				if (!as) niveau++;
				else niveau+=11;
			}
			else if (cart == 0 || cart > 10) {
				niveau += 10;
			} else  {
				niveau += cart;
			}
		}
	}
	return niveau;
};

img_create = function (src) {
    var img= document.createElement('img');
    img.src= src;
    return img;
};

window.onload = initPlay;
