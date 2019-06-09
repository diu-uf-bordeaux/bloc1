### Objets complexes

- Préparatoire: Deziper le [fichier]()

### Fichiers

- Assositation nom / contenu. Même problèmes et raisonements que nous allons tenir ici (cf. cours de système)
- Acquissition : `open`, Restitution : `close`
- Entre les deux appels a `read`/`write` qui font avancer le pointeur sur le contenu.

```python
file = open("someName.txt", mode="r")
print(file.read(42))
print(file.read(42))
file.close()
```

Note:
Bon moment pour parler/introduire de la compression ?

--

### Du texte tout simplement ?

- [ASCII]: 7 bits, c'est largement assez pour encoder tout le
  clavier américain + 32 caractères de contrôle.
  La façon dont la table est organisée est super maline
  (base 16, un espace entre maj et min)

- Les français veulent leur accents, les grecs (ou les russes) leurs
  alphabet. Principe des code page. \
  Exemple : [ISO8859] -15 latin9 (fr) -5 cyrillique

- Les chinois arrivent ... la technique ne passe pas a l'échelle

- [Unicode], et ses mises en pratiques raisonnables (UTF8/16/32).


[ASCII]: https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange
[ISO8859]: https://fr.wikipedia.org/wiki/ISO/CEI_8859
[Unicode]: https://fr.wikipedia.org/wiki/Unicode

Note:
le mot CodePage vient du numéro de page du manuel dans laqulle la table etait
imprimé (chez ibm). Les codepage les plus visible sont ceux de microsoft : 437
américain/850 latin1
Montrer le AltGr + 225 pour faire un ß

--

### Texte : ASCII

  -  | 0x0 | 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8 | 0x9 | 0xA | 0xB | 0xC | 0xD | 0xE | 0xF
-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|----
0x20 | SP  | !   |  "  |  #  |  $  |  %  |  &  |  '  |  (  |  )  |  *  |  +  |  ,  | -  | .  | /
0x30 | 0   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  :  |  ;  |  <  | =  | >  | ?
0x40 | @   | A   |  B  |  C  |  D  |  E  |  F  |  G  |  H  |  I  |  J  |  K  |  L  | M  | N  | O
0x50 | P   | Q   |  R  |  S  |  T  |  U  |  V  |  W  |  X  |  Y  |  Z  |  [  |  \  | ]  | ^  | _
0x60 | `\``  | a |  b  |  c  |  d  |  e  |  f  |  g  |  h  |  i  |  j  |  k  |  l  | m  | n  | o
0x70 | p   |  q  |  r  |  s  |  t  |  u  |  v  |  w  |  x  |  y  |  z  |  {  |  |  | }  | ~  | DEL
<!-- .element: class="stretch" style="max-width: 100%; font-size: 20px;" -->

- Un bit de plus double la taille le table. Sa signification dépend de la **code page**.
- De moins en moins utilisé.

--

### Unicode

- Défini les `code point` (caractères). La version 12.1 en contient 137994.
- UTF32: chaque caractère  est codé sur 4 octets.
- UTF8: caractères sur un nombre variable d'octets.
  - La table ASCII est sur un octet et ne bouge pas.
  - Le nombre de `1` précédent le premier zéro donne le nombre d'octets
  - La charge est codé après le premier `0` de chaque octet
  - Le prefixe `10`, sert pour les continuations -- il n'aurait pas de sens vu la propriété précédente.
  - Pas de changement pour l'existant, Robuste (pas d'état), aucun caratère n'est inclus dans un autre, moins lourd que UTF32


Note:
- La représentation d'un caractère ne peut pas être contenue dans la
  représentation d'une chaîne plus grande, ce qui permet de faire des
  recherches de sous-chaînes par comparaison d'octets, comme sur les codages à
  un octet => pas de changement de l'existant
- Un lien qui m'a aidé : https://www.figer.com/Publications/utf8.htm (DR)

--

### UTF-8: Exemple

Char. number range  |        UTF-8 octet sequence
--------------------|---------------------------------------------
0000 0000-0000 007F | 0xxxxxxx
0000 0080-0000 07FF | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


--

### Encodage chaines de caractère : Exercice

en [python](data/poem)

--

### Endianness

> Commencer par parler de Gulliver

Si on considère un octet comme indivisible, la question du comment est-il
vraiment en mémoire (au niveau du transistor) importe peu.

A partir des `short` (16 bit), la question se pose. Poids fort, ou poids faible
devant. L'un est-il mieux que l'autre ? (C'est très subjectif). Chaque fondeur
a fait son choix.

Tant qu'on est sur une même machine, finalement pas de problème. A partir du
moment ou on communique (a commencer par soi même, cas de la disquette), il
faut etre d'accord: **Protocole**.

- Réseau `bigendian` (cf. la famille de fonction `ntoh`).
- JPEG `littleendian`.

--

###  Identifier le type

- L'extension du fichier ne sert à rien. Rennomer une image ne donne pas un musique.
- On laisse des traces, des numéros magiques (`magic`). Le début du fichier est souvent un bon endroit.
- Les fichiers sont plus problèmatiques. Le `#!` (prononcer *shebang*)

> [Plein de signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

--

## Identifier le type : Exercice

Note:
Certains magics servent aussi à detecter l'endianness en un seul `read`,
0xCAFEBABE de java, ou le png.

--

## L'exemple d'un fichier audio

en [python](data/signal.py)


--

### Compression

- Hommage à la théorie de l'info.

- Destructif, non destructif
