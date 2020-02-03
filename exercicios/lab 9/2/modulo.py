from random import randint
dic = {}
def criar():
    for i in range(2,13):
        dic[i] = 0
    return dic

def lancamento():
    x = randint(1,6)
    y = randint(1,6)
    soma = x+y
    return soma    
