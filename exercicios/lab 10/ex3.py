from tkinter import *
from tkinter import messagebox

letras = {
    'a': "vogal",
    'e': "vogal",
    'i': "vogal",
    'o': "vogal",
    'u': "vogal"
}

janela = Tk()
janela.title("Classificador de letras")
janela.geometry("500x150")

letra = Label(janela, text="Letra:", font=("Arial", 12))
letra.place(relx=0.2, rely=0.2, anchor=CENTER)

entradaLetra = Entry(janela, width=14, font=("Arial", 12))
entradaLetra.place(relx=0.5, rely=0.2, anchor=CENTER)

def verificar():
    letra = entradaLetra.get()    
    if letra=="y":
        return 2
    elif letra in letras.keys():
        return 1
    elif letra == "":
        return -1
    else:
        return 0

def letra():
    tipo = verificar()

    if tipo == 0:
        res = messagebox.showinfo("Resultado", "A letra é uma consoante.")
    elif tipo == 1:
        res = messagebox.showinfo("Resultado", "A letra é uma vogal.")
    elif tipo == 2:
        res = messagebox.showinfo("Resultado", "A letra 'y' pode ser uma vogal ou uma consoante, dependendo do idioma e contexto.")
    else:
        res = messagebox.showinfo("Resultado", "Digite uma letra, por favor.")


btn = Button(janela, text='Verificar!', command=letra)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

janela.mainloop()













