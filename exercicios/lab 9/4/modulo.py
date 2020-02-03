def anagrama(x1,y1):
    dicX = {}
    dicY = {}
    cont = 0

    x = x1.lower().replace('á','a').replace('ã','a').replace('â','a').replace('é','e').replace('í','i').replace('ó','o')
    y = y1.lower().replace('á','a').replace('ã','a').replace('â','a').replace('é','e').replace('í','i').replace('ó','o')

    for i in x:
        dicX[i] = 0
    for i in y:
        dicY[i] = 0

    for i in dicX:
        for j in dicY:
            if i == j:
                cont += 1

    if cont == len(dicX):
        print(f"\n{x1} e {y1} são anagramas.")
    else:
        print(f"\n{x1} e {y1} não são anagramas.")
