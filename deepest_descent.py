from math import sqrt, pow, exp
import random
import sys
import itertools

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
        if(cont > 6):
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

# Troca dois elementos em uma lista
def troca(caminho, indice1, indice2):
	c = caminho[:]
	aux = c[indice1]
	c[indice1] = c[indice2]
	c[indice2] = aux
	return c

# Gera todos os vizinhos de um caminho
def gerarVizinhanca(caminho):
	c = caminho[:]
	vizinhanca = []
	for indice, valor in enumerate(c[1:]):
		for indice2, valor2 in enumerate(c[1:]):
			vizinho = troca(c, indice+1, indice2+1)
			if(indice != indice2 and vizinho not in vizinhanca):
				vizinhanca.append(vizinho)
	return vizinhanca

# Escolhe o melhor vizinho, dada uma vizinhanca
def escolherVizinho(vizinhanca, custos):
	melhorVizinho = []
	melhorCustoVizinho = sys.maxint
	for vizinho in vizinhanca:
		custoVizinho = calcularCustoCaminho(vizinho, custos)
		if(custoVizinho <= melhorCustoVizinho):
			melhorVizinho = vizinho
			melhorCustoVizinho = custoVizinho
	return melhorVizinho

# Funcao principal
def main():
	fileName = sys.argv[1]
	readCoords(fileName)
	createMatrix()
	caminho = range(0, len(custos))
	custoCaminho = calcularCustoCaminho(caminho, custos)

	while 1:
		vizinhanca = gerarVizinhanca(caminho)
		vizinho = escolherVizinho(vizinhanca, custos)
		custoVizinho = calcularCustoCaminho(vizinho, custos)
		if(custoVizinho <= custoCaminho):
			caminho = vizinho
			custoCaminho = custoVizinho
		else:
			break

	# Exibe o resultado
	print(caminho, custoCaminho)

# Chama a funcao principal
main()
