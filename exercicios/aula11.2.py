from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import scrolledtext

tarefas = []
seg = 59
minu_fixo = 25
minu = 24
controle = 0

def mensagem():
    res = messagebox.showinfo("Aviso!","Tarefa realizada e inserida no banco.")

def pagListar():
    janelaListar = Tk()
    janelaListar.title('Listar tarefas')
    janelaListar.geometry('400x200')
    
    label_tarefa = Label(janelaListar, text='Tarefas:', font=('Arial', 15))
    label_tarefa.place(relx=0.5, rely=0.15, anchor=CENTER)
    txt = scrolledtext.ScrolledText(janelaListar, width=40, height=5)
    txt.place(relx=0.5, rely=0.5, anchor=CENTER)

    txt.insert(0.0, '\n'.join(tarefas))

    janelaListar.mainloop()

def cadastrarTarefa():
    global tarefas
    entrada = entrada_tarefa.get()

    if entrada != '':
        tarefas.append(entrada)

def pausar():
    global controle
    if controle == 0:
        controle = 1
    else:
        controle = 0
        iniciar()

def iniciar():
    global minu, seg, controle
    if controle != 1:
        minutos['text'] = minu
        segundos['text'] = seg

        seg -= 1
            
        if minu >= 0:
            if seg == 0:
                minu -= 1
                seg = 59
            janela.after(10, iniciar)
        elif minu < 0:
            cadastrarTarefa()
            minu = minu_fixo
            seg = 59
            minutos['text'] = minu_fixo
            segundos['text'] = '00'
            mensagem()
    else:
        controle = 0

janela = Tk()
janela.title('Cronometro de Pomodoro')
janela.geometry('400x200')
menu = Menu(janela)
new_item = Menu(janela)
menu.add_cascade(label='Tarefas completas', menu=new_item)
new_item.add_command(label='Listar tarefas', command=pagListar)


label_tarefa = Label(janela, text='Tarefa:', font=('Arial', 20))
label_tarefa.place(relx=0.5, rely=0.1, anchor=CENTER)
entrada_tarefa = Entry(janela, width=45)
entrada_tarefa.place(relx=0.5, rely=0.25, anchor=CENTER)

minutos = Label(janela, text=str(minu_fixo), font=('Arial', 23))
minutos.place(relx=0.43, rely=0.60, anchor=CENTER)
pontos = Label(janela, text=':', font=('Arial', 23))
pontos.place(relx=0.49, rely=0.60, anchor=CENTER)
segundos = Label(janela, text='00', font=('Arial', 23))
segundos.place(relx=0.55, rely=0.60, anchor=CENTER)

iniciar_tarefa = Button(janela, text='Iniciar', command=iniciar)
iniciar_tarefa.place(relx=0.5, rely=0.4, anchor=CENTER)
pausar_tarefa = Button(janela, text='Pausar', command=pausar)
pausar_tarefa.place(relx=0.5, rely=0.8, anchor=CENTER)

janela.config(menu=menu)
janela.mainloop()
