from modulo import isInteger

def main():
    string = input("Digite uma string qualquer: ")

    if isInteger(string) == True:
        print("é inteiro válido.")
    else:
        print("não é inteiro válido.")
        
if __name__ == "__main__":
    main()
