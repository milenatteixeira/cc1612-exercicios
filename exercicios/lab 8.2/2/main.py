from modulo import primos

def main():
    x = int(input("digite um limite: "))

    print(f"os primos entre 2 e {x} são: ")
    print(primos(x))

if __name__ == "__main__":
    main()
