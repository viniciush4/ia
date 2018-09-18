from math import sqrt, pow, exp
import random
import sys

coords = []
custos = []



def obj(path, matriz):
    custo = 0 #acumulador
    cidadeInicial = path[0]
    for destino in path[1:]:
        custo += matriz[cidadeInicial][destino]
        cidadeinicial = destino
    custo += matriz[path[-1]][path[0]]
    return custo


def readCoords(fileName) :
    file  = open(fileName, 'r')
    cont = 0
    for line in file:
        cont = cont + 1
        #ignora a ultima linha
        if 'EOF' in line:
            break
        #Ignora as 6 primeiras linhas
        if(cont > 6):
            valores = line.split()
            #Adiciona o numero da cidade, a coordenada X e a coordenada Y
            cidade = [int(valores[0]), float(valores[1]), float(valores[2])]
            coords.append(cidade)

    file.close()


def getInitialSolution():
    return random.sample(range(len(coords)), len(coords))



def createMatrix() :
    for i, origem in enumerate(coords):
        # lista com todos os custos de uma cidade especifica para todas as outras
        cidadeCustos = []
        for j, destino in enumerate(coords):
            #se for igual o custo e zero
            if(origem[0] == destino[0]):
                cidadeCustos.append(0)
            else:
                #custo de acordo com formula de custos
                cidadeCustos.append(sqrt( pow(destino[1] - origem[1], 2) + pow(destino[2] - origem[2], 2) ))
        custos.append(cidadeCustos)


def getNeighbor(path) :
    i = random.randint(1, len(path) - 1)
    j = random.randint(1, len(path) - 1)
    while(j==i):
        j = random.randint(1, len(path) - 1)
    newPath = path.copy()
    aux = newPath[i]
    newPath[i] = newPath[j]
    newPath[j] = aux
    return newPath


def simulatedAnnealing(initialSolution, maxTemp, maxInter, tempChange, custos) :
    current = initialSolution.copy();
    cost = obj(current, custos)
    temp = maxTemp
    bestPath = current
    for i in range(maxInter):
        newPath = getNeighbor(current)
        temp = temp * tempChange
        newPathCost = obj(newPath, custos)
        currentCost = obj(current, custos)
        if (newPathCost <= currentCost or (exp(currentCost - newPathCost)/temp) > random.random()):
            current = newPath
            if newPathCost <= obj(bestPath, custos):
                bestPath = newPath

    return bestPath

def main() :
    fileName = sys.argv[1]
    initialVertex = int(sys.argv[2])
    maxTemp = 20000
    maxInter = 500
    tempChange = 0.98
    readCoords(fileName)
    createMatrix()
    initialSolution = getInitialSolution()
    initialSolution.remove(initialVertex)
    initialSolution.insert(0, initialVertex)

    bestPath = simulatedAnnealing(initialSolution, maxTemp, maxInter, tempChange, custos)
    print([bestPath, obj(bestPath, custos)])


main()
