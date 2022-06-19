from tkinter import *
from tkinter import PhotoImage

janela = Tk()

janela.title("Informa signo")
janela.geometry('480x465+610+153')
janela.resizable(height=0, width=0)

# importa imagens
imagem_fundo = PhotoImage(file="imagens\\imagem_fundo.png")
imagem_botao = PhotoImage(file="imagens\\CLIQUE PARA SABER O SIGNO.png")

# criar lagel
lab_fundo = Label(janela, image=imagem_fundo)
lab_fundo.pack()

# criar as caixas de entrada
entrada1 = Entry(janela, font=('Calibri', 23), justify=CENTER)
entrada1.place(width=123, height=54,  x=57, y=146)

entrada2 = Entry(janela, font=('Calibri', 23), justify=CENTER)
entrada2.place(width=173, height=54,  x=270, y=146)

def test():
    dia = int(entrada1.get())
    mes = entrada2.get()

    if (22 <= dia <= 31 and mes == 'dezembro') or (1 <= dia <= 20 and mes == 'janeiro'):
        n = 'Capricórnio'
    elif (21 <= dia <= 31 and mes == 'janeiro') or (1 <= dia <= 18 and mes == 'fevereiro'):
        n = 'Aquário'
    elif (19 <= dia <= 28 and mes == 'feveiro') or (1 <= dia <= 20 and mes == 'março'):
        n = 'Peixes'
    elif (21 <= dia <= 31 and mes == 'março') or (1 <= dia <= 20 and mes == 'abril'):
        n = 'Áries'
    elif (21 <= dia <= 30 and mes == 'abril') or (1 <= dia <= 20 and mes == 'maio'):
        n = 'Touro'
    elif (21 <= dia <= 31 and mes == 'maio') or (1 <= dia <= 20 and mes == 'junho'):
        n = 'Gêmeos'
    elif (21 <= dia <= 30 and mes == 'junho') or (1 <= dia <= 22 and mes == 'julho'):
        n = 'Câncer'
    elif (23 <= dia <= 31 and mes == 'julho') or (1 <= dia <= 22 and mes == 'agosto'):
        n = 'Leão'
    elif (23 <= dia <= 31 and mes == 'agosto') or (1 <= dia <= 22 and mes == 'setembro'):
        n = 'Virgem'
    elif (23 <= dia <= 30 and mes == 'setembro') or (1 <= dia <= 22 and mes == 'outubro'):
        n = 'Libra'
    elif (23 <= dia <= 31 and mes == 'outubro') or (1 <= dia <= 21 and mes == 'novembro'):
        n = 'Escorpião'
    elif (22 <= dia <= 30 and mes == 'novembro') or (1 <= dia <= 21 and mes == 'dezembro'):
        n = 'Sagitário'
    else:
        n = 'incorreto!'
    resultado['text'] = n

# Label para o resultado
resultado = Label(janela, text='', anchor='center', font=('Calibri', 23), bg='white', fg='black')
resultado.place(width=155, height=50, x=167, y=268)

# criar botão
botao = Button(janela, bd=0, image=imagem_botao, command=test)
botao.place(width=111, height=51, x=186, y=350)

janela.mainloop()
