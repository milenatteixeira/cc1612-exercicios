#interface grafica
from tkinter import *
janela = Tk()
janela.title("Conversão numérica")
janela.geometry("500x300")

#label
numeroDecimal = Label(janela, text="Número decimal:", font=("Arial", 12))
numeroDecimal.place(relx=0.2, rely=0.1, anchor=CENTER)
resposta = Label(janela, text="Resposta:", font=("Arial", 12))
resposta.place(relx=0.2, rely=0.5, anchor=CENTER)

#entrys
numDec = Entry(janela, width=14, font=("Arial", 12))
numDec.place(relx=0.5, rely=0.1, anchor=CENTER)
result = Entry(janela, width=14, font=("Arial", 12))
result.place(relx=0.5, rely=0.5, anchor=CENTER)

#funcoes
def bina():
    resultado = result.get()
    num = bin(int(numDec.get()))
    if resultado != '':
        result.delete(0, END)
        result.insert(0, str(num))
    else:
        result.insert(0, str(num))
def hexa():
    resultado = result.get()
    num = hex(int(numDec.get()))
    if resultado != '':
        result.delete(0, END)
        result.insert(0, str(num))
    else:
        result.insert(0, str(num))
def octal():
    resultado = result.get()
    num = oct(int(numDec.get()))
    if resultado != '':
        result.delete(0, END)
        result.insert(0, str(num))
    else:
        result.insert(0, str(num))

#botoes
btnBin = Button(janela, text="Binário", command=bina)
btnBin.place(relx=0.3, rely=0.3, anchor=CENTER)
btnHexa = Button(janela, text="Hexadecimal", command=hexa)
btnHexa.place(relx=0.5, rely=0.3, anchor=CENTER)
btnOct = Button(janela, text="Octal", command=octal)
btnOct.place(relx=0.7, rely=0.3, anchor=CENTER)

janela.mainloop()
