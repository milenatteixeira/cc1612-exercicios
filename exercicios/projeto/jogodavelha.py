linha = [] #variável para criação da linha da matriz como lista

jogador = 0 #variável para alternar as jogadas de cada jogador. jogador = 0 é o primeiro, jogador = 1 é o segundo

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
def jogar(player, letra, rodada):
    print()
    global jogador #aqui a variavel jogador é definida como global pois é necessário modificar o seu valor dentro de todo o código
    #input da posição em apenas um input utilizando a função split para salvar o valor antes do espaço na primeira variavel e o valor dps do espaço na segunda
    l,c = input('Digite a posiçao da onde deseja jogar, com um espaço entre os dois valores (exemplo: 0 1): ').split(' ')
    print()
    #conversão das variaveis l e c que são string para int
    l = int(l)
    c = int(c)

    #Estrutura condicional para verificar se já não há letra na posição onde o jogador escolheu
    if linha[l][c] != 'X' and linha[l][c] != 'O':
        #Caso não tenha, a posição receberá a letra do jogador correspondente e a variavel jogador irá receber o valor do proximo jogador, para alternar a jogada
        linha[l][c] = letra
        jogador = rodada
    else:
        #Caso já tenha, uma mensagem de erro é exibida e a variavel jogador continua com o mesmo valor, fazendo com que o jogador tente novamente        
        print('Posição incorreta, tente novamente!')
        print()
    imprimirMatriz() #chamada da função

#Função principal
def main():
    #Laço de repetição infinito para que o jogo pare apenas quando algum jogador ganhar
    while True:
        #Estrutura condicional para definir qual jogador irá jogar. caso a variavel esteja com o valor 0, será o primeiro. caso esteja com 1, será o segundo.
        if jogador == 0:
            print()
            print('JOGADOR 1!!')
            jogar(jogador, "X", 1)
        elif jogador == 1:
            print()
            print('JOGADOR 2!!')
            jogar(jogador, "O", 0)

        #VERIFICAÇÃO DA QUANTIDADE DE X / O NA HORIZONTAL
        if linha[0][0]== 'X' and linha[0][1]== 'X' and linha[0][2]== 'X' and linha[0][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][1]== 'X' and linha[0][2]== 'X' and linha[0][3]== 'X' and linha[0][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][0]== 'X' and linha[1][1]== 'X' and linha[1][2]== 'X' and linha[1][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][1]== 'X' and linha[1][2]== 'X' and linha[1][3]== 'X' and linha[1][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[2][0]== 'X' and linha[2][1]== 'X' and linha[2][2]== 'X' and linha[2][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[2][1]== 'X' and linha[2][2]== 'X' and linha[2][3]== 'X' and linha[2][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[3][0]== 'X' and linha[3][1]== 'X' and linha[3][2]== 'X' and linha[3][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[3][1]== 'X' and linha[3][2]== 'X' and linha[3][3]== 'X' and linha[3][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[4][0]== 'X' and linha[4][1]== 'X' and linha[4][2]== 'X' and linha[4][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[4][1]== 'X' and linha[4][2]== 'X' and linha[4][3]== 'X' and linha[4][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        if linha[0][0]== 'O' and linha[0][1]== 'O' and linha[0][2]== 'O' and linha[0][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][1]== 'O' and linha[0][2]== 'O' and linha[0][3]== 'O' and linha[0][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][0]== 'O' and linha[1][1]== 'O' and linha[1][2]== 'O' and linha[1][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][1]== 'O' and linha[1][2]== 'O' and linha[1][3]== 'O' and linha[1][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[2][0]== 'O' and linha[2][1]== 'O' and linha[2][2]== 'O' and linha[2][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[2][1]== 'O' and linha[2][2]== 'O' and linha[2][3]== 'O' and linha[2][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[3][0]== 'O' and linha[3][1]== 'O' and linha[3][2]== 'O' and linha[3][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[3][1]== 'O' and linha[3][2]== 'O' and linha[3][3]== 'O' and linha[3][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[4][0]== 'O' and linha[4][1]== 'O' and linha[4][2]== 'O' and linha[4][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[4][1]== 'O' and linha[4][2]== 'O' and linha[4][3]== 'O' and linha[4][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        #VERIFICAÇÃO DA QUANTIDADE DE X/O NA VERTICAL
        elif linha[0][0]== 'X' and linha[1][0]== 'X' and linha[2][0]== 'X' and linha[3][0]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][0]== 'X' and linha[2][0]== 'X' and linha[3][0]== 'X' and linha[4][0]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][1]== 'X' and linha[1][1]== 'X' and linha[2][1]== 'X' and linha[3][1]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][1]== 'X' and linha[2][1]== 'X' and linha[3][1]== 'X' and linha[4][1]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][2]== 'X' and linha[1][2]== 'X' and linha[2][2]== 'X' and linha[3][2]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][2]== 'X' and linha[2][2]== 'X' and linha[3][2]== 'X' and linha[4][2]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][3]== 'X' and linha[1][3]== 'X' and linha[2][3]== 'X' and linha[3][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][3]== 'X' and linha[2][3]== 'X' and linha[3][3]== 'X' and linha[4][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][4]== 'X' and linha[1][4]== 'X' and linha[2][4]== 'X' and linha[3][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][4]== 'X' and linha[2][4]== 'X' and linha[3][4]== 'X' and linha[4][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        if linha[0][0]== 'O' and linha[1][0]== 'O' and linha[2][0]== 'O' and linha[3][0]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][0]== 'O' and linha[2][0]== 'O' and linha[3][0]== 'O' and linha[4][0]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][1]== 'O' and linha[1][1]== 'O' and linha[2][1]== 'O' and linha[3][1]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][1]== 'O' and linha[2][1]== 'O' and linha[3][1]== 'O' and linha[4][1]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][2]== 'O' and linha[1][2]== 'O' and linha[2][2]== 'O' and linha[3][2]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][2]== 'O' and linha[2][2]== 'O' and linha[3][2]== 'O' and linha[4][2]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][3]== 'O' and linha[1][3]== 'O' and linha[2][3]== 'O' and linha[3][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][3]== 'O' and linha[2][3]== 'O' and linha[3][3]== 'O' and linha[4][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][4]== 'O' and linha[1][4]== 'O' and linha[2][4]== 'O' and linha[3][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][4]== 'O' and linha[2][4]== 'O' and linha[3][4]== 'O' and linha[4][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break        
        #VERIFICAÇÃO DA QUANTIDADE DE X/O NA DIAGONAL
        elif linha[0][0]== 'X' and linha[1][1]== 'X' and linha[2][2]== 'X' and linha[3][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][0]== 'X' and linha[2][1]== 'X' and linha[3][2]== 'X' and linha[4][3]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][1]== 'X' and linha[1][2]== 'X' and linha[2][3]== 'X' and linha[3][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][1]== 'X' and linha[2][2]== 'X' and linha[3][3]== 'X' and linha[4][4]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][4]== 'X' and linha[2][3]== 'X' and linha[3][2]== 'X' and linha[4][1]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][3]== 'X' and linha[1][2]== 'X' and linha[2][1]== 'X' and linha[3][0]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][4]== 'X' and linha[1][3]== 'X' and linha[2][2]== 'X' and linha[3][1]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[1][3]== 'X' and linha[2][2]== 'X' and linha[3][1]== 'X' and linha[4][0]== 'X':
            print('JOGADOR 1 VENCEU')
            break
        elif linha[0][0]== 'O' and linha[1][1]== 'O' and linha[2][2]== 'O' and linha[3][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][0]== 'O' and linha[2][1]== 'O' and linha[3][2]== 'O' and linha[4][3]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][1]== 'O' and linha[1][2]== 'O' and linha[2][3]== 'O' and linha[3][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][1]== 'O' and linha[2][2]== 'O' and linha[3][3]== 'O' and linha[4][4]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][4]== 'O' and linha[2][3]== 'O' and linha[3][2]== 'O' and linha[4][1]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][3]== 'O' and linha[1][2]== 'O' and linha[2][1]== 'O' and linha[3][0]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[0][4]== 'O' and linha[1][3]== 'O' and linha[2][2]== 'O' and linha[3][1]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        elif linha[1][3]== 'O' and linha[2][2]== 'O' and linha[3][1]== 'O' and linha[4][0]== 'O':
            print('JOGADOR 2 VENCEU')
            break
        
        
main() #chamada da função principal
input()
