Encodage : Exercice
---

### En ligne de commande

- Dans un interpreteur, affichez `fr.txt et ru.txt`
  ```bash
  cat fr.txt
  cat ru.txt
  ```

- Convertissez les en utf-8
  ```bash
  iconv -f iso-8859-15 -t utf-8 fr.txt
  iconv -f iso-8859-5 -t utf-8 ru.txt
  ```

- Sauvegardez dans un autre fichier
  ```bash
  iconv -f iso-8859-15 -t utf-8 fr.txt > fr.utf8
  iconv -f iso-8859-5 -t utf-8 ru.txt > ru.utf8
  ```
- Regardez leur taille
  ```bash
  ls -l ru.* fr.*
  ```

---

### En python

- Charger `encoding.py` dans Thonny
- En vous servant de la fonction fournie `read_file`, chargez `fr.txt`
  ```python
  read_file('fr.txt')
  ```
- Pourquoi l'interpréteur râle ?
- remédiez y en choisissant son encodage (`iso-8859-15`), et affichez le
  contenu.
- faites de même avec le `ru.txt` ... ça ne ressemble que peu à du cyrillique.
- On change l'encodage en `iso-8859-5`
- Ajouter ce code au début du main
```python
    fr = read_file('fr.txt', 'iso-8859-15')
    ru = read_file('ru.txt', 'iso-8859-5')
```

---

### Traduire le poème

- Fabriquer un fichier qui entrelace les langues
```python
with open("poem.txt", "w", encoding="utf-8") as file:
    for r, f in zip(ru, fr):
        print(r, f, file=file)
```
- *bonus*: Peut on proposer un autre encodage ? Essayez, comparez.
- Vérifiez (dans l'interpréteur) le contenu de la variable `fr`. Comparez au fichier `poem.py`. Pourquoi.
- Pour fixer le problème, au lieu d'éditer le fichier `fr.txt`, nous proposons de fusionner les lignes 3 et 4.
  ```python
  fr[3:5] = [''.join(fr[3:5])] # Les lignes 3 et 4 doivent êtres fusionnées

  ## On remplace la sous-liste (c'est cher mais c'est pas grave), de 3 à 5 (exclu)
  ## par la liste d'un élément qui est la concaténation de la sous-liste de 3 à 5
  ```
  Ou coller cette ligne ?

---

### Observer la représentation

- En vous servant de la fonction `print_binary`, affichez les infos sur le
  11ème caractère de la seconde ligne du texte `fr` en `iso-8859-15` puis en
  `utf-8`.
- Faites de même avec le tout premier caractère russe.

---

### Décortiquer un peu l'UTF-8

En vous servant de la fonction `utf8_decode` regardez les caractères suivants :

```python
# Décoder representation utf-8
utf8_decode(fr[1][10])
utf8_decode(ru[0][0])

utf8_decode(u'\u084F')
utf8_decode('\ufb79')
```

- Lire le code de la fonction `utf8_decode`
