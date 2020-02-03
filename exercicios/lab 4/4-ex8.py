from math import *
print('CÁLCULO DO PERÍMETRO DE UM POLÍGONO')
distancia = 0

x = float(input('digite a coordenada x: '))
y = float(input('digite a coordenada y: '))

x0 = x
y0 = y
while True:
    x1 = input('digite a coordenada x(em branco para sair): ')
    if x1 != '':
        x1 = float(x1)
        y1 = float(input('digite a coordenada y: '))
        distancia = distancia + sqrt(((x1-x0)**2)+((y1-y0)**2))
        x0 = x1
        y0 = y1
    else:
        distancia = distancia + sqrt(((x - x0) ** 2) + ((y - y0) ** 2))
        break
print("perímetro é: %.3f"% distancia)