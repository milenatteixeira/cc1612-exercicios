from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import messagebox

janela = Tk()
janela.geometry('470x230')
janela.title('Consumo de Energia Elétrica')

dataInicial = Label(janela, text='Data Inicial:')
dataInicial.place(relx=0.1, rely=0.1, anchor=CENTER)
dataFinal = Label(janela, text='Data Final:')
dataFinal.place(relx=0.1, rely=0.2, anchor=CENTER)
horaInicial = Label(janela, text='Hora Inicial:')
horaInicial.place(relx=0.6, rely=0.1, anchor=CENTER)
horaFinal = Label(janela, text='Hora Final:')
horaFinal.place(relx=0.6, rely=0.2, anchor=CENTER)
consTotal = Label(janela, text='Consumo Total (kWh):')
consTotal.place(relx=0.25, rely=0.8, anchor=CENTER)
consCalc = Label(janela, text='Consumo Calculado (kWh):')
consCalc.place(relx=0.25, rely=0.9, anchor=CENTER)

dInicial = Entry(janela)
dInicial.place(relx=0.32, rely=0.1, anchor=CENTER)
dFinal = Entry(janela)
dFinal.place(relx=0.32, rely=0.2, anchor=CENTER)
hInicial = Entry(janela)
hInicial.place(relx=0.82, rely=0.1, anchor=CENTER)
hFinal = Entry(janela)
hFinal.place(relx=0.82, rely=0.2, anchor=CENTER)
total = Entry(janela)
total.place(relx=0.65, rely=0.8, anchor=CENTER)
calculado = Entry(janela)
calculado.place(relx=0.65, rely=0.9, anchor=CENTER)

chuveiroEstado = BooleanVar()
chuveiroEstado.set(False)
lampadaEstado = BooleanVar()
lampadaEstado.set(False)
tomadaEstado = BooleanVar()
tomadaEstado.set(False)
arEstado = BooleanVar()
arEstado.set(False)

lampada = Checkbutton(janela, text='Lâmpadas', var=lampadaEstado)
lampada.place(relx=0.407, rely=0.55, anchor=CENTER)
chuveiro = Checkbutton(janela, text='Chuveiro', var=chuveiroEstado)
chuveiro.place(relx=0.4, rely=0.65, anchor=CENTER)
tomada = Checkbutton(janela, text='Tomadas', var=tomadaEstado)
tomada.place(relx=0.61, rely=0.55, anchor=CENTER)
ar = Checkbutton(janela, text='Ar Condicionado', var=arEstado)
ar.place(relx=0.655, rely=0.65, anchor=CENTER)

#FUNÇÕES

def aluno():
    mensagem = messagebox.showinfo("Discente", "Nome: Milena Teixeira Correia\n\nR.A: 22.219.011-8")
def limpar():
    dInicial.delete(0, END)    
    dFinal.delete(0, END)    
    hInicial.delete(0, END) 
    hFinal.delete(0, END)    
    total.delete(0, END)    
    calculado.delete(0, END)    
    chuveiroEstado.set(False)
    lampadaEstado.set(False)
    tomadaEstado.set(False)
    arEstado.set(False)
def calculo():
    arquivo = open("consumo.txt", "r")
    listaConsumo = []
    
    diaI = dInicial.get()
    horaI = hInicial.get()
    diaF = dFinal.get()
    horaF = hFinal.get()
    espacoCalculado = calculado.get()
    espacoConsumo = total.get()

    lampadaI = 0
    tomadaI = 0
    chuveiroI = 0
    arI = 0
    lampadaF = 0
    tomadaF = 0
    chuveiroF = 0
    arF = 0
    
    for linha in arquivo.readlines():
        x = linha.split()
        listaConsumo.append(x)

    for x in range(len(listaConsumo)):
        if listaConsumo[x][0] == diaI and listaConsumo[x][1] == horaI:
            if lampadaEstado.get()==True:
                lampadaI = int(listaConsumo[x][2])
            if tomadaEstado.get()==True:
                tomadaI = int(listaConsumo[x][3])
            if chuveiroEstado.get()==True:
                chuveiroI = int(listaConsumo[x][4])
            if arEstado.get()==True:
                arI = int(listaConsumo[x][5])
        if listaConsumo[x][0] == diaF and listaConsumo[x][1] == horaF:
            if lampadaEstado.get()==True:
                lampadaF = int(listaConsumo[x][2])
            if tomadaEstado.get()==True:
                tomadaF = int(listaConsumo[x][3])
            if chuveiroEstado.get()==True:
                chuveiroF = int(listaConsumo[x][4])
            if arEstado.get()==True:
                arF = int(listaConsumo[x][5])
    consumo = round(((lampadaF-lampadaI) + (tomadaF-tomadaI) + (chuveiroF-chuveiroI) + (arF-arI))/1000, 2)

    if espacoCalculado == '':
        calculado.insert(0, consumo)
    else:
        calculado.delete(0, END)
        calculado.insert(0, consumo)

    consumoTotal = (int(listaConsumo[743][2]) + int(listaConsumo[743][3]) + int(listaConsumo[743][4]) + int(listaConsumo[743][5]))/1000

    if espacoConsumo == '':
        total.insert(0, consumoTotal)
    else:
        total.delete(0, END)
        total.insert(0, consumoTotal)
        
btnCalcular = Button(janela, text='Calcular', command=calculo)
btnCalcular.place(relx=0.32, rely=0.4, anchor=CENTER)
btnLimpar = Button(janela, text='Limpar', command=limpar)
btnLimpar.place(relx=0.5, rely=0.4, anchor=CENTER)
btnAluno = Button(janela, text='Aluno', command=aluno)
btnAluno.place(relx=0.68, rely=0.4, anchor=CENTER)

janela.mainloop()
