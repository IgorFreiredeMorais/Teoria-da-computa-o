#Trabalho Prático de Teoria da Computação
#Breno Campos Barbosa
#Igor Freire de Morais
#Esse programa que simula uma máquina de Turing determinística padrão que computa funções numéricas.

#P.S:Lembrando que no argumento1.txt não pode ter espaço no início da linha
import sys

#Função que simula a máquina descrita no argumento1.txt
def maquina(transicoes,inicial,entrada,arq2):
    pos = 0 #posição na fita
    estadoAtual = inicial #estado atual da maquina
    chaves = list(transicoes.keys()) #lista com as chaves
    fita = list(entrada) #lista com a fita

    #while é percorrido enquanto existir uma transição
    while pos < len(fita) and chaves.count((estadoAtual, fita[pos])) == 1:
        acao = transicoes[(estadoAtual, fita[pos])] #acao armazena o que deve ser feito pela maquina
                                                    # acao[0] = proximo estado
                                                    # acao[1] = simbolo escrito
                                                    # acao[2] = movimento
        escreve(pos, fita,arq2,estadoAtual) #chama função que escreve a fita
        estadoAtual = acao[0] #atualiza o estado atual
        fita[pos] = acao[1] #escreve o simbolo na fita
        if(acao[2] == "L"): #movimenta a cabeça de leitura
            pos -= 1
        else:
            pos += 1

    escreve(pos, fita,arq2,estadoAtual) #escreve a fita final

#função que escreve a fita
def escreve(pos,fita,arq2,estadoAtual):
    
    saida = ""
    for c in fita: #transforma a fita em string
        if len(saida) == pos: #coloca o estado atual na saida
            saida += estadoAtual
        saida = saida + c

    #print(saida)
    arq2.write(saida + "\n")    


#COMEÇO
#abre arquivo argumento1.txt
arq = sys.argv[1]
arq = open(arq,'r')

#pula as primeiras linhas
linha = arq.readline()
for x in range(5):
    linha = arq.readline()

#cria dicionario com as transiçoes
transicoes = {} #As chaves do dicionário são o estado atual e o que esta sendo lido e os valores são o que deve ser feito pela maquina
para = True #Booleando que para o while
while para:
    linha = linha.replace("\n", "").replace("(","").replace(")","").replace(",","") #Retira tabulação e símbolos da linha
    transicao = linha.split(" ")
    transicao[0] = "{" + transicao[0] + "}" #Adiciona chaves nos estados
    transicao[3] = "{" + transicao[3] + "}"
    transicoes[(transicao[0], transicao[1])] = (transicao[3], transicao[4], transicao[5]) #Atribui chaves e valores ao dicionário
    linha = arq.readline()
    #Para o while
    if linha == "}\n":
        para = False

#pega estado inicial
linha = arq.readline()
inicial = linha.replace("\n", "")

#pega entrada
linha = arq.readline()
linha = arq.readline()
entrada = linha.replace("\n", "")

#fecha argumento1.txt
arq.close()

#abre argumento2.txt
arq2 = sys.argv[2]
arq2 = open(arq2,'w')

#Chama a função que roda a máquina
maquina(transicoes,inicial,entrada,arq2) 

#fecha o argumento2.txt
arq2.close()