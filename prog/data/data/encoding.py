
def read_file(file_name, encoding='utf-8'):
    """
    Lit un fichier codé avec `encoding` et retourne son contenu
    sous forme d'un tableau de lignes
    """
    with open(file_name, mode="r", encoding=encoding) as file:
        return file.readlines()


def print_binary(string, encoding='utf-8'):
    """
    Affiche la chaine `string` puis sa representation en base 2
    Lorsqu'elle est encodé avec `encoding`
    """
    print(string)
    print(" ".join(bit_string(string, encoding)))


def bit_string(string, encoding="utf-8"):
    """
    Retourne la liste des bytes de `string` encodé avec `encoding`.
    Les bytes sont convertis en leur representation binaire (chaine)
    """
    lst = []
    for c in string.encode(encoding):
        lst.append(format(c, '08b'))  # Alternative: bin(c)[2:]
    return lst
    # La même chose en comphension de liste
    return [format(c, '08b') for c in string.encode(encoding)]


def utf8_decode(char):
    """
    Affiche les détails de la representation d'un caractère en utf-8
    """
    assert(len(char) == 1)
    print('ord("', char, '") = ', ord(char))

    bytes_in_bits = bit_string(char)
    first_zero = bytes_in_bits[0].find('0')
    print("Nombre d'octets : ", first_zero)  # Nombre de `1` consécutifs

    val = bytes_in_bits[0][first_zero+1:]   # Le zéro ne fait pas partie de la
                                            # payload
    for byte in bytes_in_bits[1:]:  # Le premier à déjà été traité
        assert(byte[:2] == '10')
        val += byte[2:]  # Saute les 2 bits de continuations

    print("Nombre de bits significatifs extraits: ", len(val))
    print("Valeur extraite : ", int(val, 2))


if __name__ == '__main__':
    pass
