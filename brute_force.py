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
        #ignora a última linha
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


# Funcao principal
def main():
	fileName = sys.argv[1]
	readCoords(fileName)
	createMatrix()
	# Lista de vertices
	vertices = range(0, len(custos))
	# Todas as permutacoes
	permutacoes = list(itertools.permutations(vertices))
	# Menor Custo
	menorCusto = sys.maxint
	# Melhor Permutacao
	melhorPermutacao = ()

	# Para cada permutacao
	for permutacao in permutacoes:
		custo = calcularCustoCaminho(permutacao, custos)
		if(custo <= menorCusto):
			menorCusto = custo
			melhorPermutacao = permutacao
	
	# Exibe a melhor permutacao
	print(melhorPermutacao, menorCusto)

# Chama a funcao principal
main()
