def assertEquals(expected, actual, msg=None):
    """Teste l'égalité de deux valeurs, affichant un message
        si jamais elles sont différentes."""
    result = (expected == actual)
    if not result:
        print("In %s, expecting '%s', found '%s'" % (msg, expected, actual))
    return result

def run(fun, test_cases):
    """Etant donnée une fonction f et une liste de paires
       (params, retour), vérifie que f(params) == retour et
       renvoie la liste des paires pour lesquelles c'est faux."""
    return [ params
             for (params, expected, *mesg) in test_cases
             if not assertEquals(expected, fun.__call__(*params),
                                 "%s%s" % (fun.__name__, params))]