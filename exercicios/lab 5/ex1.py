lista = []
par = []
impar = []
num = 0
for i in range(20):
    num = int(input("digite um número: "))
    lista.append(num)
    if (num%2==0):
        par.append(num)
    else:
        impar.append(num)
print()
print(lista)
print()
print(par)
print()
print(impar)
