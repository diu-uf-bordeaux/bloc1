### Introduction

#### Un monde de données

- Existence d'une multitude de données à représenter&nbsp;: \
nombres, textes, sons, images ... ([si vous manquez
d'idées](https://en.wikipedia.org/wiki/List_of_file_formats))

- A l'autre extrémité, un espace de stockage qui au fond ne permet
  d'écrire que des séquences de zéros et de uns.

![IEEE754](data/images/data_repr.png) <!-- .element: class="stretch" style="max-width: 70%; vertical-align:top" -->

- Besoin de *codages* pour transcrire, décoder, et échanger toutes ces
  données.


--

### Remarque

- Les exemples utilisent des bibliothèques externes permettant
  d'accéder aux fonctions. En voici la liste :


```python
import math               # Bibliothèque standard de math
import numpy as np        # Bibliothèque numpy de calcul numérique
```

### Preparation

- Décompresser le [fichier](data/data.zip)

> Si tout s'est bien passé, vous l'avez fait durant le tp de bienvenue
