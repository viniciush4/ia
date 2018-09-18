from math import sqrt, pow, exp
import random
import sys

coords = []
custos = []

def readCoords(fileName) :
    file  = open(fileName, 'r')
    cont = 0
    for line in file:
        cont = cont + 1
        #ignora a ultima linha
        if 'EOF' in line:
            break
        #Ignora as 6 primeiras linhas
        if(cont > 8):
            valores = line.split()
            #Adiciona o numero da cidade, a coordenada X e a coordenada Y
            cidade = [int(valores[0]), float(valores[1]), float(valores[2])]
            coords.append(cidade)

    file.close()


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

# Calcula o custo de um caminho (implementacao do Lucas)
def calcularCustoCaminho(P,M):
	s=0 #acumulador
	c_ant=P[0]
	for c in P[1:]:
		s+=M[c_ant][c]
		c_ant=c
	s+=M[P[-1]][P[0]]
	return s

# Funcao principal
def main():
	fileName = sys.argv[1]
	initialVertex = int(sys.argv[2])
	readCoords(fileName)
	createMatrix()
	verticeAtual = initialVertex
	caminho = []
	while(verticeAtual != -1):
	    caminho.append(verticeAtual)
	    verticeAtual = encontrarProximoVertice(custos[verticeAtual], caminho)
	print(caminho, calcularCustoCaminho(caminho, custos))

# Encontra o proximo vertice a ser visitado
def encontrarProximoVertice(linha, verticesProibidos):
    menorCusto = sys.maxint
    menorCustoIndice = -1
    for indice, custo in enumerate(linha):
        if(indice not in verticesProibidos):
            if(custo <= menorCusto):
                menorCusto = custo
                menorCustoIndice = indice
    return menorCustoIndice

# Chama a funcao principal
main()

    


