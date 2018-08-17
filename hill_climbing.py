import sys

# Array de custos
custos = [
    [18, 12, 60, 44, 95],
    [45, 25, 76, 74, 32],
    [70, 18, 98, 10, 55],
    [30, 25, 42, 15, 64],
    [34, 52, 19, 13, 89]
]

# Vertice inicial
verticeInicial = 4

# Caminho solucao
caminho = []

# Funcao principal
def main():
	verticeAtual = verticeInicial
	while(verticeAtual != -1):
	    caminho.append(verticeAtual)
	    verticeAtual = encontrarProximoVertice(custos[verticeAtual], caminho)
	print(caminho)

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

    


