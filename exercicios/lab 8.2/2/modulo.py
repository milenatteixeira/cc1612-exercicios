x = 2
y = 10
lista = []
for i in range(x,y+1):
    lista.append(i)

for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista[i]!=lista[j]:
            if lista[i]%lista[j]==0:
                lista[j] = 0
print(lista)
                
            
