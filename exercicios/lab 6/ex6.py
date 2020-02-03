pares = open("pares.txt","w")

for x in range(999):
    if x%2==0:
        pares.write("%d\n"%x)
pares.close()

pares = open("pares.txt", "r")
impares = open("impares.txt", "w")
for linha in pares.readlines():
    x = 998-int(linha)
    impares.write("%d\n"% x)
impares.close()
pares.close()
