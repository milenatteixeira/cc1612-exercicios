#interface gráfica
from tkinter import *

janela = Tk()
janela.title("Soma")
janela.geometry("500x300")

#labels
textoX = Label(janela, text="Entre o primeiro número:", font=("Arial", 12))
textoX.place(relx=0.3, rely=0.1, anchor=CENTER)
textoY = Label(janela, text="Entre o segundo número:", font=("Arial", 12))
textoY.place(relx=0.303, rely=0.2, anchor=CENTER)
resultado = Label(janela, text="Resultado:", font=("Arial", 12))
resultado.place(relx=0.3, rely=0.3, anchor=CENTER)

#entrys
num1 = Entry(janela, width=14, font=('Arial', 12))
num1.place(relx=0.7, rely=0.1, anchor=CENTER)
num2 = Entry(janela, width=14, font=('Arial', 12))
num2.place(relx=0.7, rely=0.2, anchor=CENTER)
result = Entry(janela, width=14, font=('Arial', 12))
result.place(relx=0.7, rely=0.3, anchor=CENTER)

#funcao
def somar():
    espacoResultado = result.get()
    x = int(num1.get())
    y = int(num2.get())
    soma = x+y 

    if espacoResultado != '':
        result.delete(0, END)           
        result.insert(0, str(soma))
    else:
        result.insert(0, str(soma))

#botoes
botao = Button(janela, text='Somar!', command=somar)
botao.place(relx=0.5, rely=0.47, anchor=CENTER)

janela.mainloop()
