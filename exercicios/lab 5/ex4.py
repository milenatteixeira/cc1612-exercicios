a = "a"
num = []
neg = []
pos = []
zero = []
while True:
    a = input('digite um número (enter para sair): ')
    if a=='':
        break
    else:
        a = int(a)
        num.append(a)

for i in range(len(num)):
    if num[i]<0:
        neg.append(num[i])
    elif num[i]>0:
        pos.append(num[i])
    else:
        zero.append(num[i])

    
print(num)
print()
print(neg)
print()
print(zero)
print()
print(pos)
