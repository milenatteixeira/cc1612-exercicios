from tkinter import *
from tkinter import scrolledtext

janela = Tk()
janela.geometry("600x350")
janela.title("Algoritmo Investigativo")
cont = 0
labelPalavra = Label(janela, text="Digite a palavra a ser procurada:")
labelPalavra.place(relx=0.2, rely=0.1, anchor=CENTER)
entryPalavra = Entry(janela)
entryPalavra.place(relx=0.5, rely=0.1, anchor=CENTER)

labelQtd = Label(janela, text="Frequência:")
labelQtd.place(relx=0.2, rely=0.2, anchor=CENTER)
saidaQtd = Entry(janela)
saidaQtd.place(relx=0.5, rely=0.2, anchor=CENTER)

labelListar = Label(janela, text="Ocorrências:")
labelListar.place(relx=0.2, rely=0.3, anchor=CENTER)

listarMensagens = scrolledtext.ScrolledText(janela, width=50, height=10, font=("Arial", 10))
listarMensagens.place(relx=0.2, rely=0.58, anchor=W)

#FUNCOES
def pesquisar():
    global cont
    conversas = open("p2-chat.txt", "r")
    listaConversas = []
    palavra = entryPalavra.get()
    for linha in conversas.readlines():
        x = linha.split()
        listaConversas.append(x)
        
    for i in range(len(listaConversas)):
        for j in range(len(listaConversas[i])):
            listaConversas[i][j] = listaConversas[i][j].lower().replace('!', '').replace('.', '').replace('?', '')

    for i in range(len(listaConversas)):
        for j in range(len(listaConversas[i])):
            if palavra==listaConversas[i][j]:
                cont+=1
                listarMensagens.insert(END, listaConversas[i])
                listarMensagens.insert(END, "\n\n")
    saidaQtd.insert(0, cont)

buscar = Button(janela, text="Pesquisar!", command=pesquisar)
buscar.place(relx=0.7, rely=0.1, anchor=CENTER)

janela.mainloop()
