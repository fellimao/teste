# Algoritmos e Estruturas de Dados 2
# Gráfico Randômico Clusterizado
# Alessandra Ramires e Melissa Ribeiro 


from random import randint,choice,sample
from matplotlib import pyplot

# O método de construção do grafo utiliza alguns parâmetros, são eles:
# N o numero de vértices que o grafo terá, M o número de comunidades,
# PIn a probabilidade de conexão intra-comunidade, POut a probabilidade
# de conexão inter-comunidade e K o grau médio dos vértices do grafo.

N = int(input("Digite o número de nós: "))
M = int(input("Digite o número de comunidades: "))
K = int(input("Digite o número médio de nós: "))
POUT = float(input("Digite o valor de POut: "))
PIN = float(input("Digite o valor de PIn: "))



# Cria a matriz de adjacencia inicializada com 0
matrizAdjacencia = []
for x in range(0,N):
    matrizAdjacencia_j = []
    for y in range(0,N):
        matrizAdjacencia_j.append(0)
    matrizAdjacencia.append(matrizAdjacencia_j)

# É gerado um vetor com N vértices. 
# Os vértices de 0 até M - 1 formarão a primeira comunidade
vetorNvertices = []
for y in range(0,N):
    vetorNvertices.append(y)

# Realiza conexões enquanto o grau medio do grafo for menor que 
# o grau medio definido inicialmente pelo usuario 
k = 0
while (k < K):
    #------------------------------------------------------------------------------

    # LIGACAO INTRA-COMUNIDADE

    # Encontra o numero de vertices em cada comunidade
    # Exemplo: caso de 200 nós e 4 comunidades, cada comunidade vai ter 50 nós
    qtdVerticesNaComunidade = int(N/M)


    # Em seguida são feitas tentativas de conexão entre os vértices.
    # Primeiramente é escolhida, aleatoriamente, uma comunidade e dois vértices,
    # também aleatórios pertencentes a esta comunidade. 
    # Estes dois vértices são conectados com uma probabilidade P in
     
    # Gera um numero X para ser uma comunidade aleatoria
    comunidadeAleatoria = randint(1,M) - 1

    # Seleciona dois vetores aleatorios de uma comunidade X para que sejam os vértices
    primeiroVerticeRandomico = choice(vetorNvertices[comunidadeAleatoria*qtdVerticesNaComunidade:((comunidadeAleatoria+1)*qtdVerticesNaComunidade)])
    segundoVerticeRandomico  = choice(vetorNvertices[comunidadeAleatoria*qtdVerticesNaComunidade:((comunidadeAleatoria+1)*qtdVerticesNaComunidade)])

    # Gera uma probabilidade de conexao entre 0% e 100%
    probPin = float((sample(list(range(0, 100)),1))[0])

    # Se a probabilidade de conexao intra for menor que a probalidade inserida inicialmente
    if (probPin < PIN*100):
        # e se nao houver conexao nesses dois vertices aletorios
        if matrizAdjacencia[primeiroVerticeRandomico][segundoVerticeRandomico] == 0:
            # entao esses dois vertices aleatorios irao se conectar
            matrizAdjacencia[primeiroVerticeRandomico][segundoVerticeRandomico] = 1

    #------------------------------------------------------------------------------

    #LIGACAO INTER-COMUNIDADE

    # Gera dois vértices aleatorios
    primeiroVerticeRandomico = randint(0,N-1)
    segundoVerticeRandomico = randint(0,N-1)

    # Encontra a comunidade que o primeiro vertice aleatorio pertence
    comunidadePrimeiroVertice = int((primeiroVerticeRandomico/qtdVerticesNaComunidade) + 1)

    # Encontra a comunidade que o segundo vertice aleatorio pertence
    comunidadeSegundoVertice = int((segundoVerticeRandomico/qtdVerticesNaComunidade) + 1)

    # Esse while evita com que os vertices aleatorios gerados sejam da mesma comunidade
    while(comunidadePrimeiroVertice == comunidadeSegundoVertice):
        # gera um vertice aleatorio
        primeiroVerticeRandomico = randint(0,N-1)

        # gera um outro vertice aleatorio
        segundoVerticeRandomico = randint(0,N-1)

        # encontra a comunidade que o primeiro vertice aleatorio pertence
        comunidadePrimeiroVertice = int((primeiroVerticeRandomico / qtdVerticesNaComunidade) + 1)

        # encontra a comunidade que o segundo vertice aleatorio pertence
        comunidadeSegundoVertice = int((segundoVerticeRandomico / qtdVerticesNaComunidade) + 1)


    # Gera uma probabilidade de conexao entre 0% e 100%
    probPOut = float((sample(list(range(0, 100)),1))[0])

    # Se a probabilidade de conexao inter for menor que a probalidade inserida inicialmente
    if (probPOut < POUT*100):
        # e se nao houver conexao nesses dois vertices aletorios
        if matrizAdjacencia[primeiroVerticeRandomico][segundoVerticeRandomico] == 0:
            # entao esses dois vertices aleatorios irao se conectar
            matrizAdjacencia[primeiroVerticeRandomico][segundoVerticeRandomico] = 1

    # encontra o grau medio da matriz de adjacencia
    count = 0
    for x in range(0,N):
        for y in range(0,N):
            if (matrizAdjacencia[x][y] == 1):
                count += 1
    k = (2*count)/N # formula do grau medio
    print("O valor de k é {}".format(k,'.',2))
    #------------------------------------------------------------------------------

for linha in matrizAdjacencia:
    print(linha)

# cria dois vetores com os pontos para plotar o grafico
pontosX = []
pontosY = []
for x in range(0, N):
    for y in range(0, N):
        if (matrizAdjacencia[x][y] == 1):
            pontosX.append(x)
            pontosY.append(y)

# plot do grafico
pyplot.plot(pontosX,pontosY,'ro',markersize='2',color='white')#coloca os pontos x e y e 'ro' é grafico de bolinha
pyplot.title("Gráfico da matriz de adjacência")#titulo do grafico
pyplot.axvspan(0,N, facecolor='black', alpha=1)
pyplot.ylabel("Nós")#legenda do eixo x
pyplot.xlabel("Alessandra Ramires e Melissa Ribeiro")#legenda eixo y
pyplot.ylim(N,0)#intervalo do eixo y
pyplot.xlim(0,N)#intervalo do eixo x
pyplot.show()#plota o grafico