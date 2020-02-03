def medias(n1, n2, n3, l):    
    if l == "A":
        media = (n1+n2+n3)/3
        print("A média aritmética é %.2f" %media)
    elif l == "P":
        media = ((n1*5)+(n2*3)+(n3*2))/10
        print("A média ponderada é %.2f" %media)
    else:
        print("Letra incorreta.")

def main():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    l = input("Digite A para média aritmética ou P para média ponderada: ")
    medias(n1, n2, n3, l)
main()
