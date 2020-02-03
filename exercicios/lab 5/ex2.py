carros = ['Fusca', 'Gol', 'Vectra', 'Fox', 'Hilux']
consumo = [12, 14, 10, 9, 7]
distancia = []
preco = []
maior = consumo[0]
indice = 0

for i in consumo:
    if i>maior:
        maior=i
for i in range(5):
    if maior==consumo[i]:
        indice = i
print("o modelo mais economico é %s com %dkm por litro" % (carros[indice], maior))
for i in range(5):
    distancia.append(consumo[i] * 1000)
    preco.append(4.09 * distancia[i])
print()
for i in range(5):
    print()
    print("Carro: %s \nConsumo por litro: %d"%(carros[i],consumo[i]))
    print("Litros por 1000km: %d \nPreço a cada 1000km: %.2f" % (distancia[i], preco[i]))

