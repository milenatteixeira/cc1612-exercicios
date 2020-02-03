from modulo import confirm

def main():
    senha = input("Digite sua senha: ")

    if confirm(senha) == False:
        print("\nDigite uma nova senha.")
    else:
        print("\nSenha correta.")
    
if __name__ == "__main__":
    main()
