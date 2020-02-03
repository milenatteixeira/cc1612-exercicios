from modulo import triangulo
def main():
    c1 = float(input("Digite o primeiro cateto: "))
    c2 = float(input("Digite o segundo cateto: "))
    print("A hipotenusa é: ", triangulo(c1,c2))
    
    
if __name__ == "__main__":
    main()
