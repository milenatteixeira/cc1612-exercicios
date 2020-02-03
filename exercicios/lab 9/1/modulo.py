def procuraReversa(dic, valor):
    lista = []
    dicItens = list(dic.items())
    dicChave = list(dic.keys())
    dicValor = list(dic.values())    
    
    for i in range(len(dicValor)-1):        
        if dicValor[i]==valor:        
            x = dicChave[i]
            lista.append(x)
    return lista
        
