import sys
import itertools

# Array de custos
custos = [
    [18, 12, 60, 44, 95],
    [45, 25, 76, 74, 32],
    [70, 18, 98, 10, 55],
    [30, 25, 42, 15, 64],
    [34, 52, 19, 13, 89]
]

# Retorna o custo de uma aresta
def getCustoAresta(aresta):
	return custos[aresta[0]][aresta[1]]

# Calcula o custo de uma permutacao
def calcularCusto(permutacao):
	acumulador = 0
	for indice, vertice in permutacao:
		if(vertice != len(permutacao)-1):
			acumulador = acumulador + getCustoAresta((vertice, vertice))
	return acumulador

# Funcao principal
def main():
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
		custo = calcularCusto(permutacao)
		if(custo <= menorCusto):
			menorCusto = custo
			melhorPermutacao = permutacao
	
	# Exibe a melhor permutacao
	print(melhorPermutacao, menorCusto)

# Chama a funcao principal
main()
