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
