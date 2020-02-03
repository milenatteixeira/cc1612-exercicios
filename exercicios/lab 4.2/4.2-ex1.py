ano = int(input('digite o ano: '))
n = 1
sal = 5000
aumento = sal*0.03
if ano>=2007:
    x = (ano-2007)+1
    while n<=x:
        aumento = aumento*n + aumento
    sal = sal + (sal*aumento)
print(sal)
