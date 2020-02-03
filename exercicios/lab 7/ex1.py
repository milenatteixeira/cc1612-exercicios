while True:
    def string(x):
        x_novo = x.lower().replace(" ", "").replace("é","e").replace("à","a").replace("ã","a").replace("á","a").replace("ó","o").replace("ç","c").replace("í","i").replace("ô","o").replace("ü","u").replace("â","a").replace(",","")
        x_inverso = ""

        x_inverso = x_novo[::-1]

        print("Você digitou %s. \n"% x.lower())
        
        if x_novo == x_inverso:
            print("É palíndromo.")
        else:
            print("Não é palíndromo")
    def main():
        palavra = str(input("Digite uma palavra ou frase: "))
        string(palavra)
    main()

    op = str(input("\nDigite enter para sair, outro caracter para continuar: "))

    if op == "":
        break
    else:
        print("-------------------------***------------------------------")
        continue
