with open("ru.txt", mode="r", encoding='iso-8859-5') as file:
    ru = file.readlines()

with open("fr.txt", "r", encoding="iso-8859-15") as file:
    fr = file.readlines()

# Les lignes 3 et 4 doivent êtres fusionnées
fr[3:5] = [''.join(fr[3:5])] # Rajouter ça après
# On remplace la sous-liste (c'est cher mais c'est pas grave), de 3 à 5 (exclu)
# par la list d'un element qui est la concatenation de la sous-liste de à 5

with open("poem.txt", "w", encoding="utf-8") as file:
    for r, f in zip(ru, fr):
        print(r, f, file=file)
        
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
    return [ bin(c).lstrip('0b') for c in string.encode(encoding) ]

def utf8_decode(char):
    assert(len(char) == 1)
    bytes = bit_string(char)
    print('ord("', char, '") = ', ord(char))
    print("Nombre d'octets : ", bytes[0].find('0')) # Nombre de `1` consécutifs
    val = ""
    for byte in bytes:
        val += byte[(byte.find('0') + 1):] # Le zéro ne fait pas partie de la payload
    print("Nombre de bits significatifs: ", len(val))
    print("Valeur extraite : ", int(val, 2))


print_binary(fr[1][10], 'utf-8')
print_binary(fr[1][10], 'iso-8859-15')


print_binary(ru[0][0], 'utf-8')
print_binary(ru[0][0], 'iso-8859-5')


utf8_decode(fr[1][10])
utf8_decode(ru[0][0])

utf8_decode(u'\u084F')
utf8_decode('\ufb79')