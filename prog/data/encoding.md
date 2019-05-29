### Objets complexes

L'exemple d'un fichier audio

--

###  Identifier le type

--

### Du texte tout simplement ?

- L'octet ne faisait pas 8 bit (en anglais on parle de byte et pas d'octet)
- Transfert de 7 bits, c'est largement assez pour encoder tout le clavier américain + 32
- Les français veulent leur accents, les grecs (ou les russes) leurs alphabet. Principe des code page
- Les chinois arrivent ... la technique ne passe pas a l'échelle
- Unicode, et ses mises en pratiques raisonnables (UTF8/16/32)

--

### Endianness

> Commencer par parler de gulliver

Si on considère un octet comme indivisible, la question du comment est-il
vraiment en mémoire (au niveau du transistor) importe peu.

A partir des `short` (16 bit), la question se pose. Poid fort, ou poid faible
devant. L'un est-il mieux que l'autre ? (C'est très subjectif). Chaque fondeur
a fait son choix.

Tant qu'on est sur une même machine, finalement pas de problème. A partir du
moment ou on communique (a commencer par soi même, cas de la disquette), il
faut etre d'accord: **Protocole**.

- Réseau `bigendian` (et la famille de fonction `ntoh`).
- Jpeg `littleendian`.

--

### Compression

Hommage à la théorie de l'info.

Destructif, non destructif
