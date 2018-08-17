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

# Calcula o custo de uma permutacao
def calcularCusto(permutacao):
	if(len(permutacao) < 2):
		return 0
	acumulador = 0
	indice1 = 0
	indice2 = 1
	while(indice2 < len(permutacao)):
		acumulador = acumulador + custos[permutacao[indice1]][permutacao[indice2]]
		indice1 = indice1+1
		indice2 = indice2+1
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
		#print(permutacao,custo)
		if(custo <= menorCusto):
			menorCusto = custo
			melhorPermutacao = permutacao
	
	# Exibe a melhor permutacao
	print(melhorPermutacao, menorCusto)

# Chama a funcao principal
main()
