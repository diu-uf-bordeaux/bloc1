
def read_file(file_name, encoding='utf-8'):
    """
    Lit un fichier codé en `encoding` et retourne son contenu
    sous forme d'un tableau de lignes
    """
    with open(file_name, mode="r", encoding=encoding) as file:
        return file.readlines()

def print_binary(string, encoding='utf-8'):
    """
    Affiche la chaine `string` puis sa representation en base 2
    Lorsqu'elle est encodé en `encoding`
    """
    print(string)
    print(" ".join(bit_string(string, encoding)))

def bit_string(string, encoding="utf-8"):
    """
    Retourne la liste des bytes de `string` encodé en `encoding`.
    Les bytes sont convertis en leur representation binaire (chaine)
    """
    lst = []
    for c in string.encode(encoding):
        lst.append(format(c, '08b'))  # Alternative: bin(c)[2:]
    return lst
    ## La même chose en comphension de liste
    return [ format(c, '08b') for c in string.encode(encoding) ]


def utf8_decode(char):
    """
    Affiche les détails de la representation d'un caractère en utf-8
    """
    assert(len(char) == 1)
    print('ord("', char, '") = ', ord(char))

    bytes_in_bits = bit_string(char)
    print("Nombre d'octets : ", bytes_in_bits[0].find('0')) # Nombre de `1` consécutifs

    val = ""
    for byte in bytes_in_bits:
        val += byte[(byte.find('0') + 1):] # Le zéro ne fait pas partie de la payload

    print("Nombre de bits significatifs extraits: ", len(val))
    print("Valeur extraite : ", int(val, 2))

if __name__ == '__main__':

    # Lire le poème en francais (iso-8859-15)
    fr = read_file('fr.txt', 'iso-8859-15')
    # et l'afficher
    print(fr)

    # Idem en russe (iso-8859-5)
    ru = read_file('ru.txt', 'iso-8859-5')
    print(ru)

    # Les lignes 3 et 4 doivent êtres fusionnées
    fr[3:5] = [''.join(fr[3:5])] # Rajouter ça après
    ## On remplace la sous-liste (c'est cher mais c'est pas grave), de 3 à 5 (exclu)
    ## par la liste d'un element qui est la concatenation de la sous-liste de 3 à 5

    with open("poem.txt", "w", encoding="utf-8") as file:
        for r, f in zip(ru, fr):
            print(r, f, file=file)


    # Affiche le tableau de byte associé à qque caractères
    print_binary(fr[1][10], 'utf-8')
    print_binary(fr[1][10], 'iso-8859-15')

    print_binary(ru[0][0], 'utf-8')
    print_binary(ru[0][0], 'iso-8859-5')

    # Décoder representation utf-8
    utf8_decode(fr[1][10])
    utf8_decode(ru[0][0])

    utf8_decode(u'\u084F')
    utf8_decode('\ufb79')
