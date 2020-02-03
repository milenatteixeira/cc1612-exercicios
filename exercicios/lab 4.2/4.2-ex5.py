x = int(input('digite um número: '))

palpite = x/2

erro = ((palpite)**2) - x

while (erro > 10**-12):
    palpite = (palpite + (x/palpite))/2
    erro = ((palpite)**2) - x
print(palpite)
