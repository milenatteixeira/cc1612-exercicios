while True:
    palavra = str(input("digite uma palavra: "))
    palavra_nova = palavra.lower().replace("ã","a").replace("á","a").replace("à","a").replace("é","e").replace("â","a").replace("ô","o").replace("ó","o").replace("í","i").replace("ü","u")
    secreta = []
    palavra_achada = ""
    cont = 0

    for i in range(len(palavra)):
        secreta.append("-")
        
    while True:
        if palavra_achada!=palavra_nova:
            if cont!=5:
                x = str(input("digite a letra desejada: ")).lower()
                ctrl=0
                
                for i in range(0, len(palavra_nova), +1):    
                    if palavra_nova[i] == x: 
                        secreta[i] = x
                        ctrl=1
                        
                if ctrl==0:
                    cont+=1
                
                palavra_achada = ''.join(secreta)
                
                print(palavra_achada)
            elif cont==5:
                print("Tentativas acabaram! :(")
                break
        else:
            print("Você acertou!!")
            break
    op = str(input("Deseja jogar novamente? (s) para sim (n) para não: ")).lower()
    if op == "s":
        continue
    elif op == "n":
        print("Jogo encerrado")
        break
    else:
        print("Opção incorreta!")
        break
