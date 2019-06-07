### Objets complexes

<span class="ribbon ribbon-principle"></span>

L'exemple d'un fichier audio

--

###  Identifier le type

[plein de signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)

--

### Du texte tout simplement ?

- Le **byte** ne faisait pas 8 bit

- [ASCII]: 7 bits, c'est largement assez pour encoder tout le
  clavier américain + 32 caractères de controles.
  La façon dont la table est organisé est super maline (des puissance de 2 partout).

- Les français veulent leur accents, les grecs (ou les russes) leurs
  alphabet. Principe des code page. [ISO8859]

- Les chinois arrivent ... la technique ne passe pas a l'échelle

- [Unicode], et ses mises en pratiques raisonnables (UTF8/16/32).

- UTF8, characteres sur un nombre variable d'octet.
  La table ascii est sur un octet et ne bouge pas.  Si le bit de poit fort est
  à `1`, le nombre de `1` précédent le premier zéro donne le nombre d'octet,
  les octets suivant comment tous par `10`


[ASCII]: https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange
[ISO8859]: https://fr.wikipedia.org/wiki/ISO/CEI_8859
[Unicode]: https://fr.wikipedia.org/wiki/Unicode

Note:
le mot CodePage vient du numéro de page du manuel dans laqulle la table etait
imprimé (chez ibm). Les codepage les plus visible sont ceux de microsoft : 437
américain/850 latin1
Montrer le AltGr + 225 pour faire un ß

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

### Compression

- Hommage à la théorie de l'info.

- Destructif, non destructif
