from random import randint
m = []
r=0
for linha in range(10):
    l = []
    for coluna in range(15):
        r = randint(1,100)
        l.append(r)
    m.append(l)
print("COLUNA INTEIRA")
for linha in range(len(m)):
    for coluna in range(len(m[linha])):
        print("%4d" %m[linha][coluna], end="")
    print()
print()
print("PRIMEIRA COLUNA")
for linha in range(len(m)):
    for coluna in range(1):
        print("%4d" %m[linha][coluna], end="")
    print()
print()
