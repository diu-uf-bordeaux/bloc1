

import csv
import random


# 0 AD/CN - 1 Genre - 2 Age - 3 Score cognitif - 4 Volume HIPPocampe cm3 - 5 Volume relatif HIPPocampe %
CLASS = 0
GENDER = 1
AGE = 2
SCORE = 3
HIPPOVOL = 4
HIPPOPERCENT = 5


def importAlzheimerData(csvFileName):
    """
        importe un fichier csv contenant :
        - une ligne d'intitulés de colonnes
        - des lignes de format CLASS (string); GENDER(string); AGE(int); SCORE(float); HIPPOVOL(float); HIPPOPERCENT(float)
        voir https://docs.python.org/fr/3/library/csv.html
    """
    with open(csvFileName) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader) # liste de liste

    del data[0] # suppression des intitulés de colonnes

    for l in data:
        l[AGE] = int(l[AGE])
        l[SCORE] = int(l[SCORE])
        l[HIPPOVOL] = float(l[HIPPOVOL])
        l[HIPPOPERCENT] = float(l[HIPPOPERCENT])

    return data

def sort(data, feature):
    """ trie une liste de liste vue comme un tableau 2D, 1er indice = ligne, 2eme indice = colonne, suivant la colonne d'indice feature """
    data.sort(key= lambda l: l[feature])

def extractFeature(data, feature):
    """ extrait la colonne d'indice feature d'une liste de liste vue comme un tableau 2D, 1er indice = ligne, 2eme indice = colonne """
    return[data[i][feature] for i in range(len(data))]
    
def meanFeature(data, feature, rawBeginIndex, rawEndIndex):
    """ calcule la moyenne d'une colonne entre les lignes d'indices rawBeginIndex, rawEndIndex """
    featureData = extractFeature(data, feature)      
    sum = featureData[rawBeginIndex]
    for i in range(rawBeginIndex + 1, rawEndIndex + 1):
        sum += featureData[i]    
    return sum / (rawEndIndex - rawBeginIndex + 1)

def separateAdCn(data):
    """ teste si dans la colonne d'indice CLASS toutes les valeurs "AD" sont au début """
    n = len(data)
    for i in range(n-1):
        if data[i][CLASS] == "CN" and data[i+1][CLASS] == "AD":
            return False
    return True

def computeMeans(data, feature):
    """
        calcule la moyenne du groupe AD et la moyenne du groupe CN pour la caractéristique feature
        suppose que feature est une caractéristique numérique (AGE, SCORE, HIPPOVOL, HIPPOPERCENT)
        suppose que les deux classes apparaissent dans les données
    """
    # trie la table de façon à avoir le groupe AD au début (AD avant CN)
    sort(data, CLASS)
    # calcule l'indice du premier élément de la classe CN
    i = 0
    for l in data:
        if l[CLASS] == "CN":
            break
        i += 1
    return meanFeature(data, feature, 0, i), meanFeature(data, feature, i+1, len(data) - 1)


def classificationErrorRate(data, feature, meanAD, meanCN):
    """
       classifie chaque individu suivant la caractéristique feature et les moyennes fournies
       la classe est celle qui correspond à la moyenne la plus proche
       si cette classe est différente de celle de l'individu, il y a erreur de classification
    """
    nbErrors = 0
    for l in data :
        if abs(l[feature] - meanAD) < abs(l[feature] - meanCN) : # on classifie comme AD
            if l[CLASS] != "AD":
                nbErrors += 1
    return round(nbErrors*100/len(data))

def subList(l, listInd):
    """
       crée une sous-liste d'une liste à partir de la liste des indices des éléments à garder
    """
    subL = []
    for i in listInd:
        subL += [l[i]]
    return subL

def splitList(l, nb):
    """
       crée aléatoirement deux sous listes sans intersection à partir de la liste l
       la première contient nb éléments, la seconde len(l) - nb éléments
    """
    listInd = list(range(len(data)))
    random.shuffle(listInd) # une permutation aléatoire des indices de ligne
    lInd1 = listInd[0:nb]
    lInd2 = listInd[nb: len(data)]
    return subList(data, lInd1), subList(data, lInd2)                                 
                                 
if __name__ == '__main__':
    
    data = importAlzheimerData("Alzheimer.csv")
    n = len(data)
    
    # extraction d'une colonne
    scores = extractFeature(data, SCORE)
    print(scores)
    
    # calcul de la moyenne d'une colonne
    m = 0
    for val in scores:
        m += val
    m /= len(scores)
    
    print("moyenne des scores cognitifs : ", meanFeature(data, SCORE, 0, n-1), m)
    
    # trier suivant une colonne
    sort(data, SCORE)
    print(extractFeature(data, SCORE))
    print(extractFeature(data, CLASS))
    print(separateAdCn(data)) # trier suivant les scores ne sépare pas les deux classes mais presque!
    
    # classification
    trainingData, testingData = splitList(data, n*2//3)
    
    meanAD, meanCN = computeMeans(trainingData, SCORE)
    print("erreur score : ", classificationErrorRate(testingData, SCORE, meanAD, meanCN), "%")
    
    meanAD, meanCN = computeMeans(trainingData, HIPPOVOL)
    print("erreur volume hippocampe : ", classificationErrorRate(testingData, HIPPOVOL, meanAD, meanCN), "%")
    
    meanAD, meanCN = computeMeans(trainingData, HIPPOPERCENT)
    print("erreur volume relatif hippocampe: ", classificationErrorRate(testingData, HIPPOPERCENT, meanAD, meanCN), "%")
    
    meanAD, meanCN = computeMeans(trainingData, AGE)
    print("erreur age: ", classificationErrorRate(testingData, AGE, meanAD, meanCN), "%")
    
        