def funcao(x):
    #criaçao de dicionários
    centena = {1: 'cento',2: 'duzentos',3: 'trezentos',4: 'quatrocentos',5: 'quinhentos',6: 'seicentos',7: 'setecentos',8: 'oitocentos',9: 'novecentos'}
    dezena = {1:'dez',2:'vinte',3:'trinta',4:'quarenta',5:'cinquenta',6:'sessenta',7:'setenta',8:'oitenta',9:'noventa'}
    unidade = {1:'um',2:'dois',3:'tres',4:'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove'}
    dezdif = {10: 'dez',11:'onze',12:'doze',13:'treze',14:'catorze',15:'quinze',16:'dezesseis',17:'dezesete',18:'dezoito',19:'dezenove'}
    
    x = str(x)
    #separarando cada número em váriaveis diferentes
    
    if len(x)==3:
        x1 = int(x[0])
        x2 = int(x[1])
        x3 = int(x[2])
        sx2 = str(x2)
        sx3 = str(x3)

        y = sx2+sx3
        y = int(y)
        
        if x3!=0:
            if x2==0:
                print(f"{x} = {centena[x1]} e {unidade[x3]}")
            elif y>10 and y<20:
                print(f"{x} = {centena[x1]} e {dezdif[y]}")
            else:
                print(f"{x} = {centena[x1]} e {dezena[x2]} e {unidade[x3]}")
        elif x3==0 and x2!=0:
            print(f"{x} = {centena[x1]} e {dezena[x2]}")
        elif x=='100':
            print(f"{x} = cem")
        else:
            print(f"{x} = {centena[x1]}")
            
            
    elif len(x)==2:     
        y = int(x)      
        x1 = int(x[0])
        x2 = int(x[1])                       
        
        if x2 != 0:
            if y>10 and y<20:
                print(f"{x} = {dezdif[y]}")
            elif y>=20:                
                print(f"{x} = {dezena[x1]} e {unidade[x2]}")
        else:            
            print(f"{x} = {dezena[x1]}")
        
    elif len(x)==1:
        x = int(x)        
        if x == 0:
            print(f"{x} = zero")
        else:                        
            print(f"{x} = {unidade[x]}")
            
    else:
        print("Número incorreto!")
