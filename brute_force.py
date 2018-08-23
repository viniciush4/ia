import sys
import itertools

# Array de custos
custos = [
    [1, 1, 7, 8, 2],
    [1, 1, 5, 5, 6],
    [7, 5, 1, 2, 9],
    [8, 5, 2, 1, 7],
    [2, 6, 9, 7, 1]
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
		#print(permutacao,custo)
		if(custo <= menorCusto):
			menorCusto = custo
			melhorPermutacao = permutacao
	
	# Exibe a melhor permutacao
	print(melhorPermutacao, menorCusto)

# Chama a funcao principal
main()
