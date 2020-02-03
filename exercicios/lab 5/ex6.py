from random import randint

l = []
soma = 0
media = 0
y = 1
z = 0

for linha in range(4):
    c = []
    for coluna in range(4):
        c.append(randint(0,99))
    l.append(c)

for linha in range(len(l)):
    for coluna in range(len(l[linha])):
        print("%3d" % l[linha][coluna], end=" ")
    print()
print()

op = input("Digite uma opção. M, para média; S, para soma: ")

for linha in range(y, len(l), 1):    
    for x in range(z, len(l), 1):
        if linha<=x:
            continue
        else:
            print("%3d" % l[linha][x], end=" ")
    print()
            
if op=="M":
    for linha in range(y, len(l), 1):    
        for x in range(z, len(l), 1):
            if linha<=x:
                continue
            else:
                soma+=l[linha][x]
    media = soma/len(l)
    print("A média é: %.1f"%media)
elif op=="S":
    for linha in range(y, len(l), 1):    
        for x in range(z, len(l), 1):
            if linha<=x:
                continue
            else:
                soma+=l[linha][x]
    print("A soma é: %d" % soma)    
else:
    print("Opção incorreta, tente novamente.")

