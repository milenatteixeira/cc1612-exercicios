from tkinter import *
import math

num1 = 0
num2 = 0
sinal = ''

expressao = ''
numero = 0
janela = Tk()
janela.geometry("350x400")
janela.title("Exercício 3")
equacao = StringVar()
entrada = Entry(janela, width=30, textvariable=equacao)
entrada.place(relx=0.1, rely=0.1)

def calcular(num):
    global expressao, numero
    numero = num

    expressao += str(num)
    equacao.set(expressao)

def igual():
    global expressao, equacao
    total = str(eval(expressao))
    equacao.set(total)
    expressao = ''

def limpar():
    global expressao
    expressao = ''
    equacao.set(expressao)

b7 = Button(janela, text='7', command=lambda: calcular(7))
b7.place(relx=0.1, rely=0.2)
b8 = Button(janela, text='8', command=lambda: calcular(8))
b8.place(relx=0.2, rely=0.2)
b9 = Button(janela, text='9', command=lambda: calcular(9))
b9.place(relx=0.3, rely=0.2)
b4 = Button(janela, text='4', command=lambda: calcular(4))
b4.place(relx=0.1, rely=0.3)
b5 = Button(janela, text='5', command=lambda: calcular(5))
b5.place(relx=0.2, rely=0.3)
b6 = Button(janela, text='6', command=lambda: calcular(6))
b6.place(relx=0.3, rely=0.3)
b1 = Button(janela, text='1', command=lambda: calcular(1))
b1.place(relx=0.1, rely=0.4)
b2 = Button(janela, text='2', command=lambda: calcular(2))
b2.place(relx=0.2, rely=0.4)
b3 = Button(janela, text='3', command=lambda: calcular(3))
b3.place(relx=0.3, rely=0.4)
zero = Button(janela, text='0', command=lambda: calcular(0))
zero.place(relx=0.1, rely=0.5)

igual = Button(janela, text='=', command=igual)
igual.place(relx=0.2, rely=0.5)
limpar = Button(janela, text='C', command=limpar)
limpar.place(relx=0.3, rely=0.5)

bA = Button(janela, text='+', command=lambda: calcular("+"))
bA.place(relx=0.4, rely=0.2)
bS = Button(janela, text='-', command=lambda: calcular("-"))
bS.place(relx=0.4, rely=0.3)
bM = Button(janela, text='x', command=lambda: calcular("*"))
bM.place(relx=0.4, rely=0.4)
bD = Button(janela, text='/', command=lambda: calcular("/"))
bD.place(relx=0.4, rely=0.5)
ponto = Button(janela, text='.', command=lambda: calcular("."))
ponto.place(relx=0.4, rely=0.6)

bSe = Button(janela, text='sen', command=lambda: equacao.set(str(math.sin(numero))))
bSe.place(relx=0.53, rely=0.2)
bT = Button(janela, text='tan')
bT.place(relx=0.53, rely=0.3)
bP = Button(janela, text='^')
bP.place(relx=0.53, rely=0.4)

bC = Button(janela, text='cos')
bC.place(relx=0.67, rely=0.2)
bL = Button(janela, text='log')
bL.place(relx=0.67, rely=0.3)
bR = Button(janela, text='raiz')
bR.place(relx=0.67, rely=0.4)

janela.mainloop()
