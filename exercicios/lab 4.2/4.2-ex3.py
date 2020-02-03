n= int (input("digite valor : "))
cont=n-1
while cont>1:
    if (n %cont== 0):
        print(" não é primo !")
        break 
        cont -= 1
    else: 
        print(" é primo")
