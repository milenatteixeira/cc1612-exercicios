#Laço de repetiçao infinito para que o usuário tenha a possibilidade de escolher entre jogar novamente ou sair do jogo.
while True:
    linha = [] #variável para criação da linha da matriz como lista

    j = 0 #variável para alternar as jogadas de cada jogador. j = 0 é o primeiro, j = 1 é o segundo
    cont = 0 #contador para o número de vitorias do jogador
    #Função para imprimir as posições presentes no jogo
    def printar():
        print('                 ************** JOGO DA VELHA **************')
        print()
        print('Quadro de posições disponíveis:\n')
        for x in range(5):
            for y in range(5):
                print(x,y, end=" | ") #Aqui ele imprime os valores de x e y (que vão de 0 a 4) com um traço a cada dois números (que no caso, são as posições do jogo)   
            print() #print para pular linha
            print('----+-----+-----+-----+-----+') #print para estética/organização do quadro do jogo
        print()
    printar()
    #chamada da função 

    #Função para criar a matriz
    def criarMatriz():
        for x in range(5):
            coluna = [] #variável para criação da coluna da matriz como lista
            for y in range(5):
                coluna.append('-') #cada posição da matriz recebera a string '-' como valor
            linha.append(coluna)
    criarMatriz() #chamada da função 

    #Função para impressão da matriz
    def imprimirMatriz():
        for x in range(5):
            for y in range(5):        
                print(linha[x][y], end="      ")
            for y in range(5):
                print(x,y, end=" | ")    
            print()
            print('                                   ----+-----+-----+-----+-----+')

    #Função onde ocorre o jogo
    #A função recebe como parametro a variavel jogador inicializada no começo do código, a letra de cada jogador e a rodada, que servirá para mudar o valor da
    #variavel jogador
    def jogar(player, nome, letra, rodada):
        print()
        global j #aqui a variavel j é definida como global pois é necessário modificar o seu valor dentro de todo o código
        #input da posição em apenas um input utilizando a função split para salvar o valor antes do espaço na primeira variavel e o valor dps do espaço na segunda
        
        print('Jogador da vez: %s' %nome) #print pro nome do jogador
        
        l,c = input('Digite a posiçao da onde deseja jogar, com um espaço entre os dois valores (exemplo: 0 1): ').split(' ')
        print()
        #conversão das variaveis l e c que são string para int
        l = int(l)
        c = int(c)

        #Estrutura condicional para verificar se já não há letra na posição onde o jogador escolheu
        if linha[l][c] != 'X' and linha[l][c] != 'O':
            #Caso não tenha, a posição receberá a letra do jogador correspondente e a variavel jogador irá receber o valor do proximo jogador, para alternar a jogada
            linha[l][c] = letra
            j = rodada
        else:
            #Caso já tenha, uma mensagem de erro é exibida e a variavel jogador continua com o mesmo valor, fazendo com que o jogador tente novamente        
            print('Posição incorreta, tente novamente!')
            print()
        imprimirMatriz() #chamada da função
    #funçao para manipular arquivos. os parametros sao o nome do jogador (para abrir seu arquivo) e a variavel x que é um contador que recebe um valor sempre
    #que o jogador ganha
    def arquivo(nome, x):
        
        arquivo = open('quantidades de vitorias do jogador %s.txt'%nome,'r') #aqui abre o arquivo do jogador como leitura

        lista = arquivo.readlines() #a variavel lista recebe o valor presente no arquivo
        arquivo.close() #fecha o arquivo
        
        arquivo = open('quantidades de vitorias do jogador %s.txt'%nome,'w') #abertura do arquivo como escrita

        #estrutura condicional para verificar se há elementos dentro da lista/arquivo
        if len(lista)!=0:
            #se tiver elementos, a variavel y recebe o valor que estiver dentro do arquivo
            y  = int(lista[0])
            y+=x # a variavel y é somada com o valor do contador passado como parametro 
            arquivo.write('%d'%y) #o arquivo recebe de volta o valor atualizado
        #caso nao tenha elementos, o arquivo recebe o valor da primeira vitoria que é igual a 1
        else:
            arquivo.write('1')
    #funçao para imprimir o numero de vitorias dos jogadores
    def imprimirVitorias(nome): #o parametro da funçao é o nome do jogador
        arquivo = open('quantidades de vitorias do jogador %s.txt'%nome,'r') #abertura do arquivo do jogador como leitura
        lista = arquivo.readlines() #a variavel lista recebe o valor presente no arquivo

        #estrutura condicional para verificar se a lista está vazia ou nao
        #se nao estiver vazia, a variavel y recebe o valor que estiver na lista como inteiro e imprime o nome e a quantidade de vitorias do jogador
        if len(lista)!=0:
            y = int(lista[0])
            print('O jogador %s tem o total de %d vitórias!!'%(nome,y))
        #se estiver vazio significa que o jogador nao venceu ainda e isso é informado pelo print
        else:
            print('O jogador %s não tem vitórias ainda.'%nome)
    #Função principal
    def main():
        global cont #contador global
        jogador = input("Digite o nome do primeiro jogador: ") #nome do jogador 1
        outrojogador = input("Digite o nome do segundo jogador: ") #nome do jogador 2

        arq = open('quantidades de vitorias do jogador %s.txt'%jogador,'a') #criaçao e abertura do arquivo como leitura e escrita
        arq2 = open('quantidades de vitorias do jogador %s.txt'%outrojogador,'a')
        imprimirVitorias(jogador)#chamada da funçao para imprimir vitorias
        imprimirVitorias(outrojogador)
        #Laço de repetição infinito para que o jogo pare apenas quando algum jogador ganhar
        while True:
            #Estrutura condicional para definir qual jogador irá jogar. caso a variavel esteja com o valor 0, será o primeiro. caso esteja com 1, será o segundo.
            if j == 0:
                print()
                jogar(j, jogador, "X", 1)
            elif j == 1:
                print()
                jogar(j, outrojogador, "O", 0)

            #VERIFICAÇÃO DA QUANTIDADE DE X / O NA HORIZONTAL
            if linha[0][0]== 'X' and linha[0][1]== 'X' and linha[0][2]== 'X' and linha[0][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1 #contador que recebe mais um valor toda vez que o jogador ganha
                arquivo(jogador, cont) #chamada da funçao com o nome do jogador e o contador  como parametro
                break
            elif linha[0][1]== 'X' and linha[0][2]== 'X' and linha[0][3]== 'X' and linha[0][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][0]== 'X' and linha[1][1]== 'X' and linha[1][2]== 'X' and linha[1][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][1]== 'X' and linha[1][2]== 'X' and linha[1][3]== 'X' and linha[1][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[2][0]== 'X' and linha[2][1]== 'X' and linha[2][2]== 'X' and linha[2][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[2][1]== 'X' and linha[2][2]== 'X' and linha[2][3]== 'X' and linha[2][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[3][0]== 'X' and linha[3][1]== 'X' and linha[3][2]== 'X' and linha[3][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[3][1]== 'X' and linha[3][2]== 'X' and linha[3][3]== 'X' and linha[3][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[4][0]== 'X' and linha[4][1]== 'X' and linha[4][2]== 'X' and linha[4][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[4][1]== 'X' and linha[4][2]== 'X' and linha[4][3]== 'X' and linha[4][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][0]== 'O' and linha[0][1]== 'O' and linha[0][2]== 'O' and linha[0][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][1]== 'O' and linha[0][2]== 'O' and linha[0][3]== 'O' and linha[0][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][0]== 'O' and linha[1][1]== 'O' and linha[1][2]== 'O' and linha[1][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][1]== 'O' and linha[1][2]== 'O' and linha[1][3]== 'O' and linha[1][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[2][0]== 'O' and linha[2][1]== 'O' and linha[2][2]== 'O' and linha[2][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[2][1]== 'O' and linha[2][2]== 'O' and linha[2][3]== 'O' and linha[2][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[3][0]== 'O' and linha[3][1]== 'O' and linha[3][2]== 'O' and linha[3][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[3][1]== 'O' and linha[3][2]== 'O' and linha[3][3]== 'O' and linha[3][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[4][0]== 'O' and linha[4][1]== 'O' and linha[4][2]== 'O' and linha[4][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[4][1]== 'O' and linha[4][2]== 'O' and linha[4][3]== 'O' and linha[4][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            #VERIFICAÇÃO DA QUANTIDADE DE X/O NA VERTICAL
            elif linha[0][0]== 'X' and linha[1][0]== 'X' and linha[2][0]== 'X' and linha[3][0]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][0]== 'X' and linha[2][0]== 'X' and linha[3][0]== 'X' and linha[4][0]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][1]== 'X' and linha[1][1]== 'X' and linha[2][1]== 'X' and linha[3][1]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][1]== 'X' and linha[2][1]== 'X' and linha[3][1]== 'X' and linha[4][1]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][2]== 'X' and linha[1][2]== 'X' and linha[2][2]== 'X' and linha[3][2]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][2]== 'X' and linha[2][2]== 'X' and linha[3][2]== 'X' and linha[4][2]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][3]== 'X' and linha[1][3]== 'X' and linha[2][3]== 'X' and linha[3][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][3]== 'X' and linha[2][3]== 'X' and linha[3][3]== 'X' and linha[4][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][4]== 'X' and linha[1][4]== 'X' and linha[2][4]== 'X' and linha[3][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][4]== 'X' and linha[2][4]== 'X' and linha[3][4]== 'X' and linha[4][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][0]== 'O' and linha[1][0]== 'O' and linha[2][0]== 'O' and linha[3][0]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][0]== 'O' and linha[2][0]== 'O' and linha[3][0]== 'O' and linha[4][0]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][1]== 'O' and linha[1][1]== 'O' and linha[2][1]== 'O' and linha[3][1]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][1]== 'O' and linha[2][1]== 'O' and linha[3][1]== 'O' and linha[4][1]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][2]== 'O' and linha[1][2]== 'O' and linha[2][2]== 'O' and linha[3][2]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][2]== 'O' and linha[2][2]== 'O' and linha[3][2]== 'O' and linha[4][2]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][3]== 'O' and linha[1][3]== 'O' and linha[2][3]== 'O' and linha[3][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][3]== 'O' and linha[2][3]== 'O' and linha[3][3]== 'O' and linha[4][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][4]== 'O' and linha[1][4]== 'O' and linha[2][4]== 'O' and linha[3][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][4]== 'O' and linha[2][4]== 'O' and linha[3][4]== 'O' and linha[4][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break        
            #VERIFICAÇÃO DA QUANTIDADE DE X/O NA DIAGONAL
            elif linha[0][0]== 'X' and linha[1][1]== 'X' and linha[2][2]== 'X' and linha[3][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][0]== 'X' and linha[2][1]== 'X' and linha[3][2]== 'X' and linha[4][3]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][1]== 'X' and linha[1][2]== 'X' and linha[2][3]== 'X' and linha[3][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][1]== 'X' and linha[2][2]== 'X' and linha[3][3]== 'X' and linha[4][4]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][4]== 'X' and linha[2][3]== 'X' and linha[3][2]== 'X' and linha[4][1]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][3]== 'X' and linha[1][2]== 'X' and linha[2][1]== 'X' and linha[3][0]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][4]== 'X' and linha[1][3]== 'X' and linha[2][2]== 'X' and linha[3][1]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[1][3]== 'X' and linha[2][2]== 'X' and linha[3][1]== 'X' and linha[4][0]== 'X':
                print('%s VENCEU'%jogador)
                cont+=1
                arquivo(jogador, cont)
                break
            elif linha[0][0]== 'O' and linha[1][1]== 'O' and linha[2][2]== 'O' and linha[3][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][0]== 'O' and linha[2][1]== 'O' and linha[3][2]== 'O' and linha[4][3]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][1]== 'O' and linha[1][2]== 'O' and linha[2][3]== 'O' and linha[3][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][1]== 'O' and linha[2][2]== 'O' and linha[3][3]== 'O' and linha[4][4]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][4]== 'O' and linha[2][3]== 'O' and linha[3][2]== 'O' and linha[4][1]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][3]== 'O' and linha[1][2]== 'O' and linha[2][1]== 'O' and linha[3][0]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[0][4]== 'O' and linha[1][3]== 'O' and linha[2][2]== 'O' and linha[3][1]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
            elif linha[1][3]== 'O' and linha[2][2]== 'O' and linha[3][1]== 'O' and linha[4][0]== 'O':
                print('%s VENCEU'%outrojogador)
                cont+=1
                arquivo(outrojogador, cont)
                break
        arq.close() #fechamento dos arquivos
        arq2.close()
            
    main() #chamada da função principal
    print()
    #input pra opcao do usuario
    op = input("Deseja jogar novamente? (s para sim, n para não)")
    #estrutura condicional. se a opçao for sim, ele volta pro começo do loop. se for nao, ele dá um aviso de erro e para o programa.
    if op == 's':
        continue
    elif op == 'n':
        print('Jogo finalizado.')
        break
    print()
input()
