---
title: Traitement du signal en python
---

### En ligne de commande

Regarder les premiers octets du fichier `signal_bruite.wav`

```python
hexdump -C signal_bruite.wav | head
```

### Acquisition des données

- Ouvrir un nouveau fichier et le sauver sous `signal.py`

```python
file = open("signal_bruite.wav", mode="rb")
```

- Lire l'en-tête (44 octets)

```python
header = file.read(44)
```

- Quel est son type ?

- Afficher les magics:
  - les 4 premiers caractères
  - les 4 caractères commençant au 9ème
  - et les 3 suivants.

```python
print(header[:4], header[8:12], header[12:15])
```

- Construire un `int` depuis les 4 octets commençant au 4ème

- Affichez le, et comparez le à la taille du fichier \
  (`ls -l signal_bruite.wav`). Il faut donc corriger.

```python
data_len = int.from_bytes(header[4:8], "little") - (44 - 8)
```

- Lire les données. Discuter les avantages/inconvénients des deux appels suivant.

```python
file.read()         # Lit jusqu'à la fin du fichier
file.read(data_len) # Lit `data_len` byte
```

- Transformer les `bytes` en liste d'entier

```python
data = list(file.read())
assert(data_len == len(data))
```

- On n'a plus besoin du fichier, on le ferme

```python
file.close()
```

### Afficher les données

- Afficher les 99 premiers points (on pourrait tout afficher mais ça
  demanderait plus de manipulation pour voir des choses).

```python
import matplotlib.pyplot as mp # Importe la partie plot de la bibliothèque matplotlib

mp.plot(data[:100])

mp.show()
```

### Filtrer le signal

(avant le `mp.show()`)

- Construire la liste `data_filtered`, ou chaque point par la moyenne du
  précédent, courant et suivant. *Remarque:* les extrémités sont inchangées.

### Corrigé

Nous vous fournissons un [corrigé], s'il vous plait. Attendez le cours de
programmation pour le regarder

[Corrigé]: data/signal.py
