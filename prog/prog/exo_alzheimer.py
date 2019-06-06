import csv
import random

# Constantes utilisées dans ce module
CLASS = 0         # AD == malade / CN == contrôle
GENDER = 1        # Genre
AGE = 2           # Age
SCORE = 3         # Score cognitif
HIPPOVOL = 4      # Volume HIPPocampe (en cm3)
HIPPOPERCENT = 5  # Volume relatif HIPPocampe (en %, entre 0 et 1)


def importAlzheimerData(csvFileName):
    """
        Importe un fichier csv contenant :
        - une ligne d'intitulés de colonnes
        - des lignes de format CLASS (string); GENDER(string); AGE(int);
                      SCORE(float); HIPPOVOL(float); HIPPOPERCENT(float)
        (voir https://docs.python.org/fr/3/library/csv.html)
    """
    data = []
    with open(csvFileName) as csvfile:
        csvfile.readline() # Skip header
        reader = csv.reader(csvfile, delimiter=';')
        for class_, sex, age, score, hippovol, hippopc in reader:
            data.append([class_, sex, int(age), int(score), float(hippovol), float(hippopc)])
    return data


def sort(data, feature):
    """ Trie une liste d'enregistrements vue comme un tableau 2D,
        (1er indice = ligne, 2eme indice = colonne)
        suivant la colonne d'indice `feature`. """
    data.sort(key= lambda l: l[feature])


def extractFeature(data, feature):
    """ Extrait la colonne d'indice `feature` d'une liste
        d'enregistrements vue comme un tableau 2D
        (1er indice = ligne, 2eme indice = colonne) """
    # return[data[i][feature] for i in range(len(data))]
    return [l[feature] for l in data]


def meanFeature(data, feature, rawBeginIndex, rawEndIndex):
    """ Calcule la moyenne d'une colonne entre les lignes
        d'indices rawBeginIndex et rawEndIndex de la liste `data`."""
    assert((rawBeginIndex >= 0) and
           (rawEndIndex >= rawBeginIndex) and
           (rawEndIndex < len(data)))
    featureData = extractFeature(data, feature)
    sum = featureData[rawBeginIndex]
    for i in range(rawBeginIndex + 1, rawEndIndex + 1):
        sum += featureData[i]
    return sum / (rawEndIndex - rawBeginIndex + 1)


def separateAdCn(data):
    """ Teste si dans la colonne d'indice CLASS,
        toutes les valeurs "AD" sont au début. """
    n = len(data)
    for i in range(n-1):
        if data[i][CLASS] == "CN" and data[i+1][CLASS] == "AD":
            return False
    return True


def containBothClasses(data):
    """ Teste si la liste `data` contient bien des données
        appartenant aux deux classes AD et CN. """
    ads = [ d for d in data if d[CLASS] == "AD" ]
    cns = [ d for d in data if d[CLASS] == "CN" ]
    return (len(ads) > 0) and (len(cns) > 0)


def computeMeans(data, feature):
    """
        Calcule la moyenne du groupe AD et du groupe CN
        pour la caractéristique `feature`.
        Suppose que feature est une caractéristique numérique
                            (AGE, SCORE, HIPPOVOL, HIPPOPERCENT)
        Suppose que les deux classes apparaissent dans les données.
    """
    # Trie la table de façon à avoir le groupe AD au début (AD avant CN)
    sort(data, CLASS)
    # Calcule l'indice du premier élément de la classe CN
    i = 0
    for l in data:
        if l[CLASS] == "CN":
            break
        i += 1
    return meanFeature(data, feature, 0, i), \
        meanFeature(data, feature, i+1, len(data) - 1)


def classificationErrorRate(data, feature, meanAD, meanCN):
    """
       Classifie chaque individu dans `data` suivant la caractéristique
       `feature` et les moyennes fournies.
       La classe est celle qui correspond à la moyenne la plus proche.
       Il y a erreur de classification si cette classe est différente
       de celle de l'individu.
    """
    nbErrors = 0
    for l in data:
        if abs(l[feature] - meanAD) < abs(l[feature] - meanCN): # on classifie comme AD
            if l[CLASS] != "AD":
                nbErrors += 1
    return round(nbErrors*100/len(data))


def subList(l, listInd):
    """
       Crée une sous-liste d'une liste `l` à partir de la liste des
       indices des éléments à conserver.
    """
    subL = []
    for i in listInd:
        subL += [l[i]]
    return subL


def splitList(l, nb):
    """
       Crée aléatoirement deux sous listes sans intersection à partir
       d'une liste `l`. La première contient nb éléments, la seconde
       len(l) - nb éléments.
    """
    listInd = list(range(len(data)))
    random.shuffle(listInd) # Une permutation aléatoire des indices de ligne
    lInd1 = listInd[0:nb]
    lInd2 = listInd[nb: len(data)]
    return subList(data, lInd1), subList(data, lInd2)


################################################################
if __name__ == '__main__':

    data = importAlzheimerData("Alzheimer.csv")
    n = len(data)

    # Extraction d'une colonne
    scores = extractFeature(data, SCORE)
    print(scores)

    # Calcul de la moyenne d'une colonne
    m = 0
    for val in scores:
        m += val
    m /= len(scores)

    print("Moyenne des scores cognitifs : ", meanFeature(data, SCORE, 0, n-1), m)

    # Trie les données selon leur SCORE
    sort(data, SCORE)
    print(extractFeature(data, SCORE))
    print(extractFeature(data, CLASS))
    # Trier suivant les scores ne sépare pas les deux classes mais presque!
    print("Le score sépare les classes ? : %s" % (separateAdCn(data),))

    # Classification
    trainingData, testingData = splitList(data, n*2//3)

    # Vérification
    if (not containBothClasses(trainingData)) or \
       (not containBothClasses(testingData)):
        raise "Découpage des données incorrect"

    # Affichage des résultats
    meanAD, meanCN = computeMeans(trainingData, SCORE)
    print("Erreur score : ",
          classificationErrorRate(testingData, SCORE,
                                  meanAD, meanCN), "%")

    meanAD, meanCN = computeMeans(trainingData, HIPPOVOL)
    print("Erreur volume hippocampe : ",
          classificationErrorRate(testingData, HIPPOVOL,
                                  meanAD, meanCN), "%")

    meanAD, meanCN = computeMeans(trainingData, HIPPOPERCENT)
    print("Erreur volume relatif hippocampe: ",
          classificationErrorRate(testingData, HIPPOPERCENT,
                                  meanAD, meanCN), "%")

    meanAD, meanCN = computeMeans(trainingData, AGE)
    print("Erreur age: ",
          classificationErrorRate(testingData, AGE,
                                  meanAD, meanCN), "%")
