from modulo import procuraReversa

def main():
    dic = {
        'um': 1,
        'dois': 2,
        'tres': 2,
        'quatro': 4
        }
    valor = int(input("digite o valor que quer buscar: "))
    print(procuraReversa(dic,valor))

if __name__ == '__main__':
    main()
