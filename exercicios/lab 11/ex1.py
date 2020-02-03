from tkinter import *
from datetime import datetime

janela = Tk()
janela.geometry("300x200")
janela.title("Exercício 1")

hora = Label(janela)
hora.place(relx=0.5, rely=0.3, anchor=CENTER)

data = Label(janela)
data.place(relx=0.5, rely=0.5, anchor=CENTER)



def att():
    x = datetime.now()    
    time = x.strftime("%H:%M:%S")
    date = x.strftime("%d/%m/%Y")
    hora['text'] = time
    data['text'] = date

    janela.after(1000, att)

att()
janela.mainloop()
