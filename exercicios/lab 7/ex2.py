arquivo = open("Python.txt","r", encoding="utf-8")
lista = arquivo.readlines()
arquivo.close()
x2 = ""
x3 = ""
lista2 = []
lista3 = []
tam = []

for x in lista:
    x2 = x.lower().strip().replace(".", "").replace("é","e").replace("à","a").replace("ã","a").replace("á","a").replace("ó","o").replace("ç","c").replace("í","i").replace("ô","o").replace("ü","u").replace("â","a").replace(",","")
    lista2.append(x2)

for x in range(len(lista2)):
    x3 = lista2[x].split()
    lista3.append(x3)
    
for x in range(len(lista3)):
    for y in range(len(lista3[x])):
        tamanho = len(lista3[x][y])
        tam.append(tamanho)
        
print("o maior numero de letras em uma palavra do arquivo é",max(tam))
print("as palavras com o maior numero de letras sao")
for x in range(len(lista3)):
    for y in range(len(lista3[x])):
        if len(lista3[x][y]) == max(tam):            
            print(lista3[x][y])

