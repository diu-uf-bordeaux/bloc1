fname = "/tmp/signal_bruite.wav"

file = open(fname, mode="rb")
# On ouvre le fichier nommé `fname` en lecture (`r`)
# et en mode binaire (b), i.e., retourne des bytes (pas d'encodage).

# L'en tête d'un fichier wave fait 44 octets
header = file.read(44)

# Les 4 premiers contienent la chaine `RIFF`
# Les 4 suivants contienent la longueur du fichier - 8 (la position courrante)
#     et en little endian
# Les 4 suivant contienent la chaine `WAVE`
print(header[:4], header[8:12])

# on construit un int depuis la longueur ... et on le corrige pour le ramener a
# la taille du signal
data_len = int.from_bytes(header[4:9], "little") - (44 - 8)

# on lit le fichier ; puis on construit une liste a partir des donnée lues
data = list(file.read(data_len)) # Optional and 'll read

# On ferme le fichier
file.close()

# On charge la lib (normalement on ferait ça dans le main ou en haut)
import matplotlib.pyplot as mp

# On affiche les 99 premiers points (c'est déprimant)
mp.plot(data[:100])

# Pour le plaisir, on filtre en appliquant une moyenne
data_filtered = [ data[i] if i == 0 or i == data_len else int(sum(data[i-1 : i+2]) / 3.0)
                  for i in range(data_len) ]
# Note: On pourrait faire un map de range aussi ... ca serait pas plus moche

mp.plot(data_filtered[:100])

# On peut maintenant voir le travail du filtre
mp.show()
