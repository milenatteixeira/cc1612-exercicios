from modulo import doacao
def main():
    s = input("Digite seu sexo: ")
    sexo = s.lower()
    peso = float(input("Digite seu peso: "))
    doacao(sexo,peso)


if __name__ == "__main__":
    main()
