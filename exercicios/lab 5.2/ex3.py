p = []
while True:
    palavra = input('digite uma palavra (enter para sair):')
    if palavra != '':
        if palavra not in p:
            p.append(palavra)
    else:
        print(p)
        break
