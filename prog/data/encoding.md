### Objets complexes
#### Fichiers

- Un fichier associe un **chemin** (un nom) à son contenu concret. \
  Il est encore une fois question de représentation des données.

- Acquisition d'un pointeur sur le contenu du fichier : `open`.
- Restitution et nettoyage : `close`
- Entre les deux, appels à `read`/`write` qui font avancer le pointeur
  sur le contenu.

```python
file = open("poem.py", mode="r")       # acquisition (mode lecture)
print(file.read(9))                    # '\ndef read'
print(file.read(9))                    # '_file(fil'
file.close()                           # restitution
```

- Pour obtenir des bytes, lire en [mode](https://docs.python.org/3/library/functions.html#open) binaire (`mode="rb"`).

Note:
Bon moment pour parler/introduire de la compression ?

--

### Endianness

La valeur `0xDEADBEEF` peut s'écrire :

*#octet*    |  1     |    2   |   3    |  4
-------------|--------|--------|--------|-------
**big**      | `0xDE` | `0xAD` | `0xBE` | `0xEF`
**little**   | `0xEF` | `0xBE` | `0xAD` | `0xDE`

- Le protocole doit spécifier l'ordre&nbsp;:
  - Les protocoles réseau utilisent généralement *big endian*
    (cf. la famille de fonction `ntoh`, *network to harware*).
  - Les types de fichiers `jpeg`/`wave` veulent *little endian*.

- En Python, on peut fabriquer un `int` a partir de `bytes`

```python
int.from_bytes(b'\x10\x00', byteorder='big', signed=False)  # -> 4096
```

Note:
- Commencer par parler de Gulliver

- Si on considère un octet comme indivisible, la question du comment est-il
  vraiment en mémoire (au niveau du transistor) importe peu.
- A partir des `short` (16 bit), la question se pose. Poids fort, ou poids faible
  devant. L'un est-il mieux que l'autre ? (C'est très subjectif). Chaque fondeur
  a fait son choix.

- Tant qu'on est sur une même machine, finalement pas de problème. A partir du
  moment ou on communique (a commencer par soi même, cas de la disquette), il
  faut etre d'accord: **Protocole**.

- Technique de la multiplication dans un sens ou dans l'autre.
  Mieux avec des decalages et des masques.

--

### Texte

- Associer un nombre à une lettre nécessite des standards

- [ASCII] : définit le représentation de 7 bits

- [ISO-8859] : définit une famille de représentation avec un 8ème bit
  (double la taille)

  - La représentation dépend de sa **code page**. Les plus connues des
  français : `iso-8859-15`, `iso-8859-1`.
  - De moins en moins utilisé.

- [Unicode]: définit les caractères comme des **code points**. La
  version 12.1 en contient 137994 😀.
  - UTF-32: chaque caractère  est codé sur 4 octets.

[ASCII]: https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange
[ISO-8859]: https://fr.wikipedia.org/wiki/ISO/CEI_8859
[Unicode]: https://fr.wikipedia.org/wiki/Unicode

Note:
- 7 bits, c'est largement assez pour encoder tout le
  clavier américain + 32 caractères de contrôle.
  La façon dont la table est organisée est super maline
  (base 16, un espace entre maj et min)
- Un constat, on veut des accents !
- Les français veulent leur accents, les grecs (ou les russes) leurs
  alphabet. Principe des code page (nom venant de la page de manuel d'IBM
  ou elles étaient imprimé à l'origine).  437 américain/850 devenu latin1
- Un bit de plus double la taille le table.
- Montrer/parler le AltGr + 225 pour faire un ß
- Les chinois arrivent ... la technique ne passe pas a l'échelle

--
### Texte : ASCII


<div class="stretch center" style="font-size: 22px;">

&nbsp;   | 0x0 | 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8 | 0x9 | 0xA | 0xB | 0xC | 0xD | 0xE | 0xF
-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|----
**0x20** | SP  | !   |  "  |  #  |  $  |  %  |  &  |  '  |  (  |  )  |  *  |  +  |  ,  | -  | .  | /
**0x30** | 0   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  :  |  ;  |  <  | =  | >  | ?
**0x40** | @   | A   |  B  |  C  |  D  |  E  |  F  |  G  |  H  |  I  |  J  |  K  |  L  | M  | N  | O
**0x50** | P   | Q   |  R  |  S  |  T  |  U  |  V  |  W  |  X  |  Y  |  Z  |  [  |  \  | ]  | ^  | _
**0x60** | \`  | a   |  b  |  c  |  d  |  e  |  f  |  g  |  h  |  i  |  j  |  k  |  l  | m  | n  | o
**0x70** | p   |  q  |  r  |  s  |  t  |  u  |  v  |  w  |  x  |  y  |  z  |  {  |  \| | }  | ~  | DEL

</div>

> Il est fortement recommandé d'**éviter** de nommer des
  identificateurs avec autre chose que des caractères ASCII.

Note:
- Python 3 le tolère par défaut
- Essayez de lire du code en japonais/chinois ... avec des emojis

--

### Encodage Unicode: UTF-8

- Caractères sur un nombre variable d'octets.
  - Le nombre de `1` précédent le premier zéro donne le nombre d'octets
    - Avec un cas particulier pour `0` qui veut dire 1 octet.
  - La charge (*payload*) est codée après le premier `0` de chaque octet en *bigendian*
  - Le préfixe `10`, sert pour les continuations

- Pas de changement pour l'existant: la table ASCII ne bouge pas,
le code d'UNIX n'a pas besoin d'être changé.
- Robuste (pas d'état), moins lourd que UTF-32.

Note:
- La représentation d'un caractère ne peut pas être contenue dans la
  représentation d'une chaîne plus grande, ce qui permet de faire des
  recherches de sous chaînes par comparaison d'octets, comme sur les codages à
  un octet => pas de changement de l'existant
- Un lien qui m'a aidé : https://www.figer.com/Publications/utf8.htm (DR)

--

### UTF-8: Exemple

> Extrait de la [RFC-3629]

Char. number range  |        UTF-8 octet sequence
--------------------|---------------------------------------------
0000 0000-0000 007F | 0xxxxxxx
0000 0080-0000 07FF | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
<!-- .element: class="small" -->

[RFC-3629]: https://tools.ietf.org/html/rfc3629

--

### Encodage chaînes de caractères : Python

- Convertir une chaîne en tableau de `bytes` en spécifiant l'encodage

```python
mes_bytes = "Ça".encode('iso-8859-15')  #  b'\xc7a'
```

- Construire une chaîne depuis un tableau de `bytes` en spécifiant l'encodage

```python
str(mes_bytes, 'iso-8859-15')  # "Ça"
```

- Pour l'appliquer à toutes les lectures et les écritures d'un fichier texte (`mode="t"`)

```python
open(filename, mode="r", encoding="utf-8")
```

> Exercice: [poem](data/poem).

--

###  Identifier le type d'un fichier

- L'extension du fichier n'est pas significative
  - Renommer une image ne donne pas une chanson.

- On laisse des traces, des numéros magiques (`magic`).
  - Le début du fichier est souvent un bon endroit.

> [Plein de signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

- Les fichiers textes n'ont usuellement pas de signature.
  - Certains débutent par un `#!` (prononcer *shebang*)
    qui désigne l'interpréteur à utiliser pour lire le fichier.

Note:
- Pratique pour rendre un script directement utilisable

--

### Identifier le type : Exercice

Magic | extension | Type
------|-----------|------
`ID3` | `.mp3`    | MP3 file
`PK`  | `.zip` | Archive Zip
`MZ`  | `.exe`    | Exécutable windows
`.ELF`|           | Exécutable linux
`%PDF-` | `.pdf`  | Adobe PDF Document
`0xFFD8FF` | `.jpeg`  | Fichier JPEG
`0xCAFEBABE` | `.class` | Classes java
||

- Recherchez le type des fichiers du répertoire `guess` en utilisant `hexdump -C nom_de_fichier | head`

Note:
- servent aussi à détecter l'*endianness* en un seul `read`,
0xCAFEBABE de java
- Renommez les fichier pour les essayer
- la réponse la plus rapide est bien sur `file guess/*`

--

## L'exemple d'un fichier audio

#### Anatomie

- En-tête de 44 octets
  - commençant par `RIFF`
  - Suivi de la longueur de la suite (4 octets *little endian*)
  - deux magics de plus `WAVE`, `fmt`
  - Le format audio (1: `pcm`)
  - Le nombre de pistes, la fréquence, le nombre de bits par ...
- Ici, le signal pcm brut 8 bit, mono

> Exercice: [signal](data/signal)

--

### Compression

- Réduire le nombre de bits pour représenter l'information.
- Utilisé à la fois pour le stockage et le transfert.
- Nécessite de décompresser
- Profite d'une connaissance a priori sur la source

- Usages:
  - Sans perte : Archivage
    - Ça ne sert à rien de re-compresser.
  - Avec perte : Signal (image, son, vidéo ...)

- Exemple d'algorithmes : RLE, Huffman, Lempel-Ziv ...

Note:
On peut remarquer un cas hybride du jpeg
- Transformée en ondelettes (~fourier)
- on crée beaucoup de zéros, quantification (enlève les poids pas assez fort)
- On lit en diagonale pour avoir le plus de zéros a la fin, et on ne les encode pas.
- Sur tout ça on applique Huffman
