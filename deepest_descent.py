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

def troca(caminho, indice1, indice2):
	aux = valor
	caminho[indice1] = caminho[indice2]
	caminho[indice2] = aux

def gerarVizinhanca(caminho):
	vizinhanca = []
	for indice, valor in enumerate(caminho[1:]):
		for indice2, valor2 in enumerate(caminho[1:]):
			aux = valor
			caminho[indice] = valor2
			caminho[indice2] = aux
			vizinhanca.append(caminho)
			caminho[indice2] = aux
			

# Funcao principal
def main():
	caminho = range(0, len(custos))
	custoCaminho = calcularCustoCaminho(caminho, custos)
	
	while 1:
		vizinhanca = gerarVizinhanca(caminho)
		vizinho = escolherVizinho(vizinhanca)
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
