import csv
import random
import statistics
import matplotlib.pyplot

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
    return [l[feature] for l in data]

def filterData(data, feature, val):
    """ Extrait les lignes pour lesquelles la colonne d'indice `feature`
        a pour valeur `val` dans une liste d'enregistrements vue comme
        un tableau 2D  (1er indice = ligne, 2eme indice = colonne) """
    return [l for l in data if l[feature] == val]


def separateClasses(data):
    """ Teste si dans la colonne d'indice CLASS,
        toutes les valeurs "AD" sont au début. """
    n = len(data)
    for i in range(n-1):
        if data[i][CLASS] == "CN" and data[i+1][CLASS] == "AD":
            return False
    return True


def containsBothClasses(data):
    """ Teste si la liste `data` contient bien des données
        appartenant aux deux classes AD et CN. """
    ads = filterData(data, CLASS, "AD")
    cns = filterData(data, CLASS, "CN")
    return (len(ads) > 0) and (len(cns) > 0)


def computeMean(data, group, feature):
    """
        Calcule la moyenne des données de la classe `group` pour la caractéristique `feature`.
        Suppose que feature est une caractéristique numérique (AGE, SCORE, HIPPOVOL, HIPPOPERCENT)
    """
    
    dataGroup = filterData(data, CLASS, group)
    return statistics.mean(extractFeature(dataGroup, feature))
    
                    
def classificationErrorRate(testData, feature, meanAD, meanCN):
    """
       Classifie chaque individu dans `testData` suivant la caractéristique
       `feature` et les moyennes fournies.
       La classe est celle qui correspond à la moyenne la plus proche.
       Il y a erreur de classification si cette classe est différente
       de celle de l'individu.
    """
    nbErrors = 0
    for l in testData:
        if abs(l[feature] - meanAD) < abs(l[feature] - meanCN): # on classifie comme AD
            if l[CLASS] != "AD":
                nbErrors += 1
    return round(nbErrors*100/len(testData))


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
    listInd = list(range(len(l)))
    random.shuffle(listInd) # Une permutation aléatoire des indices de ligne
    lInd1 = listInd[0:nb]
    lInd2 = listInd[nb: len(l)]
    return subList(l, lInd1), subList(l, lInd2)

def classificationErrorRateForFeature(trainingData, testingData, feature):
    meanAD, meanCN = computeMean(trainingData, "AD", feature), computeMean(trainingData, "CN", feature)
    return classificationErrorRate(testingData, feature, meanAD, meanCN)


################################################################
if __name__ == '__main__':

    data = importAlzheimerData("Alzheimer.csv")
    n = len(data)
    # Extraction d'une colonne
    scores = extractFeature(data, SCORE)
    print(scores)

    # Calcul de la moyenne d'une colonne
    print("Moyenne des scores cognitifs : ", statistics.mean(scores))

    # Trie les données selon leur SCORE
    sort(data, SCORE)
    # print(extractFeature(data, SCORE))
    # print(extractFeature(data, CLASS))
    # Trier suivant les scores ne sépare pas les deux classes mais presque!
    print("Le score sépare les classes ? : %s" % (separateClasses(data),))

    # Classification
    trainingdata, testingdata = splitList(data, n*2//3)

    # Vérification
    if (not containsBothClasses(trainingdata)) or \
       (not containsBothClasses(testingdata)):
        raise "Découpage des données incorrect"

    # Affichage des résultats
    
    print("Erreur score cognitif : ", classificationErrorRateForFeature(trainingdata, testingdata, SCORE), "%")
    print("Erreur volume hippocampe : ", classificationErrorRateForFeature(trainingdata, testingdata, HIPPOVOL), "%")
    print("Erreur volume relatif hippocampe: ", classificationErrorRateForFeature(trainingdata, testingdata, HIPPOPERCENT), "%")
    print("Erreur age: ", classificationErrorRateForFeature(trainingdata, testingdata, AGE), "%")

    dataAD = filterData(data, CLASS, "AD")
    scoresAD = extractFeature(dataAD, SCORE)
    dataCN = filterData(data, CLASS, "CN")
    scoresCN = extractFeature(dataCN, SCORE)
    
    matplotlib.pyplot.hist(scoresAD)
    matplotlib.pyplot.hist(scoresCN)
    
    matplotlib.pyplot.show()
    
    volumesAD = extractFeature(dataAD, HIPPOVOL)
    volumesCN = extractFeature(dataCN, HIPPOVOL)
    matplotlib.pyplot.hist(volumesAD)
    matplotlib.pyplot.hist(volumesCN)
    matplotlib.pyplot.show()
    