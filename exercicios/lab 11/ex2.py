from tkinter import *
from tkinter import Menu
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext

janela = Tk()
janela.geometry("500x300")
janela.title("Exercício 2")

chk_state = BooleanVar()
chk_state2 = BooleanVar()
chk_state3 = BooleanVar()
chk_state4 = BooleanVar()
chk_state.set(False)
chk_state2.set(False)
chk_state3.set(False)
chk_state4.set(False)

chk = Checkbutton(janela, text='Ar condicionado', var=chk_state)
chk.place(relx=0.58, rely=0.1)
chk2 = Checkbutton(janela, text='Direção hidráulica', var=chk_state2)
chk2.place(relx=0.58, rely=0.2)
chk3 = Checkbutton(janela, text='Rádio', var=chk_state3)
chk3.place(relx=0.58, rely=0.3)
chk4 = Checkbutton(janela, text='Airbag', var=chk_state4)
chk4.place(relx=0.58, rely=0.4)

marca = Label(janela, text='Marca:')
marca.place(relx=0.1, rely=0.1, anchor=CENTER)
modelo = Label(janela, text='Modelo:')
modelo.place(relx=0.1, rely=0.2, anchor=CENTER)
ano = Label(janela, text='Ano:')
ano.place(relx=0.1, rely=0.3, anchor=CENTER)
placa = Label(janela, text='Placa:')
placa.place(relx=0.1, rely=0.4, anchor=CENTER)
km = Label(janela, text='Km:')
km.place(relx=0.1, rely=0.5, anchor=CENTER)

m = Entry(janela)
m.place(relx=0.2, rely=0.1)
mO = Entry(janela)
mO.place(relx=0.2, rely=0.2)
a = Entry(janela)
a.place(relx=0.2, rely=0.3)
p = Entry(janela)
p.place(relx=0.2, rely=0.4)
k = Entry(janela)
k.place(relx=0.2, rely=0.5)

def cad():
    marca = m.get()
    modelo = mO.get()
    ano = a.get()
    placa = p.get()
    km = k.get()    

    if chk_state.get()==True:
        chk = "Ar condicionado"
    else:
        chk = ''
    if chk_state3.get()==True:
        chk2 = "Direção hidráulica"
    else:
        chk2 = ''
    if chk_state3.get()==True:
        chk3 = "Rádio"
    else:
        chk3 = ''
    if chk_state4.get()==True:
        chk4 = "Airbag"
    else:
        chk4 = ''    
    
    arquivo = open('%s.txt'%placa, 'a')
    arquivo.write("Marca: %s\nModelo: %s\nAno: %s\nPlaca: %s\nKm: %s\nCom: %s %s %s %s"%(marca, modelo, ano, placa, km, chk, chk2, chk3, chk4))
    arquivo.close()
    
def buscar():
    telaBuscar=Tk()
    telaBuscar.geometry('500x300')
    telaBuscar.title('Buscar carro por placa')
    
    placa = Label(telaBuscar, text='Digite a placa:')
    placa.place(relx=0.1, rely=0.1, anchor=CENTER)
    p = Entry(telaBuscar)
    p.place(relx=0.2, rely=0.08)
    txt = scrolledtext.ScrolledText(telaBuscar, width=55, height=10)
    txt.place(relx=0.5, rely=0.55, anchor=CENTER)

    def achar():        
        placa = p.get()
        arquivo = open('%s.txt'%placa, 'r')

        carros = arquivo.readlines()
        
        txt.insert(0.0, ''.join(carros))

    btn = Button(telaBuscar, text='Buscar', command=achar)
    btn.place(relx=0.7, rely=0.07)    
    telaBuscar.mainloop()
    
btn = Button(janela, text='Cadastrar veículo', command=cad)
btn.place(relx=0.4, rely=0.7)

menu = Menu(janela)
new_item = Menu(janela)
menu.add_cascade(label='Buscar carro', menu=new_item)
new_item.add_command(label='Buscar por placa', command=buscar)

janela.config(menu=menu)
janela.mainloop()
