temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
menor= temperaturas[0]
maior= temperaturas[0]
soma = 0
for i in temperaturas:
    if i < menor:
        menor = i
    if i > maior:
        maior = i
    soma = i + soma
media = soma/(len(temperaturas))
print('o menor é o %d, o maior é o %d e a média é %.2f'%(menor, maior, media))
