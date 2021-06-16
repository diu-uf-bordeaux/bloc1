### Modules

- Besoin de structure pour partager et réutiliser du code.

- Regroupe un ensemble de fonctions (classes, modules) dans un même module, i.e., un fichier.

- Importer un module rend les fonctions du module accessible au module courant.

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
Message
- Copier/coller des fonctions c'est pas top
- Un fichier, okay on peut faire un répertoire ...

Syntaxe: un mot sur le `as`

--

### Fabriquer un module

<a href='https://docs.python.org/3/tutorial/modules.html' class='ribbon ribbon-ref'></a>

fact.py <!-- .element: class="title" -->
```python
def fact(n):
    """Renvoie le produit des entiers de 1 à n"""
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)
```

binomial.py <!-- .element: class="title" -->
```python
import fact from fact

def binomial(n, k):
    """Retourne le coéfficient binomial de n et k"""
    if k > n:
        k, n = n, k  # Mais qui à laissé ce swap
    return fact(n) / (fact(n)*fact(n - k))

if __name__ == '__main__'
    n, k = int(input()), int(input())      # Bouuuh
    # from sys import argv                 # Importer la ligne de commande
    # n, k = int(argv[1]), int(argv[2])    # Les valeurs commencent à [1:]
    print("C(%s, %s) = %s" % (k, n, binomial(k, n)))

```

Note:
- Pourquoi `input` n'est pas la meilleure idée du monde
- Comment le remplacer par une ligne de commande :
  - `from sys import argv` (apres le `if main`)
  - `n, k = int(argv[1]), int(argv[2])`

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
