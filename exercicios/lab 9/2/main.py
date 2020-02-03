from modulo import criar, lancamento

def main():
    dic = criar()
    cont = 0
    for x in range(1,1001):
        soma = lancamento()
        dic[soma] += 1
    print("Soma   |   Qtd   |  Porcentagem")
    for x, y in dic.items():
        print(f"   {x}       {y}          %.2f%%" % ((y*100)/1000))
    

if __name__ == "__main__":
    main()
