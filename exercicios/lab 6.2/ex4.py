num = []
num_unicos = []

def ler():
    arquivo = open('numeros4.txt', 'r')

    for x in arquivo.readlines():
        num.append(int(x))
        
    return num

def norepetion(num):
    for x in num:
        while x not in num_unicos:
            num_unicos.append(x)
    return num_unicos

def escrita(num_unicos):
    arquivo = open('numeros4unicos.txt','w')
    for x in num_unicos:
        arquivo.write('%d \n'%x)
    arquivo.close()

def main():
    ler()
    norepetion(num)
    escrita(num_unicos)
    
main()

