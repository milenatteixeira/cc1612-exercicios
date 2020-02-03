def arquivos():
    arquivo = open("numeros3.txt","r")
    somatoria = 0
    listaArquivo = arquivo.readlines()
    for x in listaArquivo:
        somatoria += float(x)        
    media = somatoria/len(listaArquivo)
    print("A somatória dos números é %.2f e a média é, aproximadamente, %.2f"%(somatoria, media))
    arquivo.close()
arquivos()
