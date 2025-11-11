# Importando Tkinter 
from tkinter import *
from tkinter import ttk

# cores 

cor1 = '#3b3b3b' # black/preta
cor2 = '#feffff' # white/branca
cor3 = '#38576b' # Azul carregado
cor4 = '#ECEFF1' # Cizenta
cor5 = '#FFAB40' # Orange/Laranja


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310') # Tamanho da calculadora
janela.config(bg=cor1)

# Primeiro frame

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

# Segundo Frame

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variavel todos valores

todos_valores = ''


# Label

valor_texto = StringVar()

# Função

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    
    
    # Passando valor para tela da calculadora
    valor_texto.set(todos_valores)



# Função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

# Função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')




app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)



# Botões

b_1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0) # Botão 'C' (limpar tela)
b_2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda:entrar_valores('%'))
b_2.place(x=118, y=0) # Botão '%' (resto da divisão)
b_3 = Button(frame_corpo, text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda:entrar_valores('/'))
b_3.place(x=177, y=0) # Botão '/' (Divisão)

b_4 = Button(frame_corpo, text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda:entrar_valores('7'))
b_4.place(x=0, y=52) # Botão '7' (Número 7)
b_5 = Button(frame_corpo, text='8', width= 5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda:entrar_valores('8'))
b_5.place(x=59, y=52) # Botão '8' (Número 8)
b_6 = Button(frame_corpo, text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('9'))
b_6.place(x=118, y=52) # Botão '9' (Número 9)
b_7 = Button(frame_corpo, text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= lambda: entrar_valores('*'))
b_7.place(x=177, y=52) # Botão '*' (Asterisco)

b_8 = Button(frame_corpo, text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('4'))
b_8.place(x=0, y=104) # Botão '4' (Número 4)
b_9 = Button(frame_corpo, text='5', width=5, height=2, bg=cor4, font=('iVY 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valores('5'))
b_9.place(x=59, y=104) # Botão '5' (Número 5)
b_10 = Button(frame_corpo, text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entrar_valores('6'))
b_10.place(x=118, y=104) # Botão '6' (Número 6)
b_11 = Button(frame_corpo, text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('-'))
b_11.place(x=177, y=104) # Botão '-' (Subtração)

b_12 = Button(frame_corpo, text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('1'))
b_12.place(x=0, y=156) # Botão '1' (Número 1)
b_13 = Button(frame_corpo, text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('2'))
b_13.place(x=59, y=156) # Botão '2' (Número 2)
b_14 = Button(frame_corpo, text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('3'))
b_14.place(x=118, y=156) # Botão '3' (Número 3)
b_15 = Button(frame_corpo, text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('+'))
b_15.place(x=177, y=156) # Botão '+' (Adição)

b_16 = Button(frame_corpo, text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('0'))
b_16.place(x=0, y=208) # Botão '0' (Zero)
b_17 = Button(frame_corpo, text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=lambda:entrar_valores('.'))
b_17.place(x=118, y=208) # Botão '.' (Ponto)
b_18 = Button(frame_corpo, text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,command=calcular)
b_18.place(x=177, y=208) # Botão '=' (Igual)

# Lógica das operações artiméticas 




























janela.mainloop()
