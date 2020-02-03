palavra = input("digite uma palavra: ")
lista = ["paciencia","paçoca","ufologia","eclipse","economia","vacilar","vagabundo","jaboti"]
def strcmp(palavra, lista):
    return(palavra in lista)
print(strcmp(palavra,lista))
