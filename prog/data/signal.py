fname = "signal_bruite.wav"

file = open(fname, mode="rb")
# On ouvre le fichier nommé `fname` en lecture (`r`)
# et en mode binaire (b), i.e., retourne des bytes (pas d'encodage).

# L'en tête d'un fichier wave fait 44 octets
header = file.read(44)

# Les 4 premiers contienent la chaine `RIFF`
# Les 4 suivants contienent la longueur du fichier - 8 (la position courrante)
#     et en little endian
# Les 4 suivant contienent la chaine `WAVE`
print(header[:4], header[8:12], header[12:15])

# on construit un int depuis la longueur ... et on le corrige pour le ramener a
# la taille du signal
data_len = int.from_bytes(header[4:8], "little") - (44 - 8)
print("Longueur attendue : ", data_len)

# on lit le fichier ; puis on construit une liste a partir des donnée lues
data = list(file.read())
assert(data_len == len(data))

# On ferme le fichier
file.close()

# On charge la lib (normalement on ferait ça dans le main ou en haut)
import matplotlib.pyplot as mp

# On affiche les 99 premiers points (c'est déprimant)
mp.plot(data[:100])

# Pour le plaisir, on filtre en appliquant une moyenne
bounds = [0, data_len - 1]
data_filtered = [data[i] if i in bounds else int(sum(data[i-1:i+2]) / 3.0)
                 for i in range(data_len)]
mp.plot(data_filtered[:100])


def dot_product(v1, v2):
    return sum([i*j for i, j in zip(v1, v2)])


avg_filter = [1/3, 1/3, 1/3]

data_filtered_dot = [data[i]
                     if i in bounds
                     else int(dot_product(data[i-1:i+2], avg_filter))
                     for i in range(data_len)]

mp.plot(data_filtered_dot[:100])

# On peut maintenant voir le travail du filtre
smp.show()
