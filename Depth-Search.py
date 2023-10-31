class Vertice:
    def __init__(self):
        self.adj = []
        self.cor = str("BRANCO")
        self.pred = None
        self.descoberta = None
        self.termino = None


tempo = int(0)
Ciclo = int(0)
topologica = []
component = ['|']


def cria_Grafo(Max_v, Max_a):
    Grafo = {}

    for i in range(Max_v):
        Grafo[i] = Vertice()

    for k in range(Max_a):
        entrada = input()
        aux = entrada.split(" ")
        Grafo[int(aux[0])].adj.append(int(aux[1]))

    return Grafo


def profundidade_Visit(Vertice, Grafo, atual):
    global tempo
    tempo = tempo + 1
    Vertice.cor = "CINZA"
    Vertice.descoberta = tempo

    for k in range(len(Vertice.adj)):
        aux = int(Vertice.adj[k])
        if (Grafo[aux].cor == "BRANCO"):
            Grafo[aux].pred = int(atual)
            profundidade_Visit(Grafo[aux], Grafo, aux)
        if (Grafo[aux].cor == "CINZA"):
            global Ciclo
            Ciclo = Ciclo + 1
    Vertice.cor = "PRETO"
    tempo = tempo + 1
    Vertice.termino = tempo
    global topologica
    topologica.append(atual)


def Profundidade(Grafo):
    for j in range(len(Grafo)):
        if (Grafo[j].cor == "BRANCO"):
            profundidade_Visit(Grafo[j], Grafo, j)
    return Grafo

def Profundidade_2(Grafo, topologica):
    global tempo
    tempo = 0
    for j in range(len(topologica)):
        if (Grafo[topologica[j]].cor == "BRANCO"):
            component.append(topologica[j])
            Componentes(Grafo[topologica[j]], Grafo, topologica[j])
            component.append("|")
    return Grafo


def Transposto(Grafo):
    transposto = {}
    for j in range(len(Grafo)):
        transposto[j] = Vertice()

    for i in range(len(Grafo)):
        for k in range(len(Grafo[i].adj)):
            aux = Grafo[i].adj[k]
            transposto[aux].adj.append(i)
    return transposto
    

def Componentes (Vertice, Grafo, atual):
    Vertice.cor = "CINZA"
    for k in range(len(Vertice.adj)):
        aux = int(Vertice.adj[k])
        if (Grafo[aux].cor == "BRANCO"):
            component.append(aux)
            Componentes(Grafo[aux], Grafo, aux)
    Vertice.cor = "PRETO"
    

Tamanhos = input()
Tamanhos = Tamanhos.split(" ")

Graph = cria_Grafo(int(Tamanhos[0]), int(Tamanhos[1]))

Teste = Profundidade(Graph)

print("Tempos:")

for i in range(len(Teste)):
    print(i, ":", Teste[i].descoberta, "/", Teste[i].termino)

print("\nNumero de ciclos:", Ciclo, "\n")

if (Ciclo == 0):
    print("Ordenacao topologica:")
    print(topologica[::-1], "\n")
else:
    print("Nao possui ordenacao topologica.\n")

Exe = Transposto(Teste)

topologic = topologica[::-1]

Profundidade_2(Exe, topologic)

print("Componentes:", component)