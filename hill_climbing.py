import sys

# Array de custos
custos = [
    [1, 1, 7, 8, 2],
    [1, 1, 5, 5, 6],
    [7, 5, 1, 2, 9],
    [8, 5, 2, 1, 7],
    [2, 6, 9, 7, 1]
]

# Vertice inicial
verticeInicial = 0

# Caminho solucao
caminho = []

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
	verticeAtual = verticeInicial
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

    


