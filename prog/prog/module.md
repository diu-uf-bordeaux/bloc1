### Modules

- Besoin de structure pour partager et réutiliser du code.

- Regroupe un ensemble de fonctions (classes, modules) dans un même module, i.e., un fichier.

- Importer un module, rends les fonctions du module accessible au module courant.

- Pour éviter les conflits de noms, les **espaces de noms** permettent de lever
  les ambigüités. Le module est aussi un espace de nom.

<div class='half' style='width: 33%;'>

```python
import sys

print(sys.argv)
```

</div><div class='half' style='width: 33%;'>

```python
from sys import argv

print(argv)
```

</div><div class='half' style='width: 33%;'>

```python
from sys import *
# mimicracra
print(path)
```

</div>

Note:
- Copier/coller des fonctions c'est pas top
- Un fichier, okay on peut faire un répertoire ...

--

### Fabriquer un module

https://docs.python.org/3/tutorial/modules.html

--

### Modules : remarques

- Le module par défaut (*toplevel*) se nomme `__main__`

- Les importations se font en fonction de la variable `sys.path`

- L'import `*` est relativement dangereux, il pollue rapidement l'espace de
  nom. Pour mitiger cet effet, les noms commencant par `_` ne sont pas
  importés. Il sont néamoins accessible par leur nom qualifié. \
  Exemple: `sys._git`

- On peut structurer en répertoire plutôt qu'en fichier, le code doit alors se
  trouver dans un fichier `__init__.py`
