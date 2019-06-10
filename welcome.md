---
title: TP de bienvenue
---

## TP de Bienvenue

<style>
code {
  color: #aa2222;
}
</style>

---

1. *Logguez*-vous

2. Ouvrir un navigateur (XXXXX) et faites le pointer vers : <br/>
  <https://diu-uf-bordeaux.github.io/bloc1/>

3. Ouvrez un terminal (si, si, il ne va pas vous mordre)

4. Créez un répertoire `data`.
  - Pour créer un répertoire : `mkdir xxxx`
  > Les informaticiens n'aiment pas trop les majuscules et vraiment pas les espaces.

5. Puis rendez-vous y.
  - Changer de répertoire : `cd xxxx`
  - Vérifier ou vous êtes : `pwd`
  - Revenir dans votre maison : `cd`
  - Remonter d'un répertoire : `cd ..`

6. A partir de maintenant, nous considérons que vous êtes dans le répertoire `data`

7. Téléchargez l'archive [suivante](xxxxx).
  - Si vous voulez le faire en ligne de commande :
  ```python
  wget xxxxx
  ```

8. Décompressez l'archive
  - Soit en clic-o-drome
  - ou avec `unzip xxxx.zip`

9. Listez les fichiers : `ls`
    - Et avec plus d'information : `ls -l`

10. Lancez `thonny`
  - Idéalement `thonny &`
  > Le `&` permet de lancer le programme en tâche de fond.

11. Occupez vous ...
    - Ouvrir un nouveau fichier, le sauvegarder sous le nom `welcome.py`
    - Copiez/collez le code suivant :
    ```python
    def mystere1(lst):
        for i in range(1, len(lst)):
          if lst[i] < lst[i - 1]:
            return False
        return True
    ```
    - Chargez le ... en appuyant sur `F5`
    - Que fait cette fonction ?
    > Indice, exectuez là avec des valeurs.
    > Par exemple `[1, 3, 20, 42]`, et `[1, 3, -20, 42]`
