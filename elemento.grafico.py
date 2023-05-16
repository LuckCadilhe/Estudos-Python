from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal =  Tk()
texto = Label(master= janelaPrincipal, text = "Minha janela exibidia")
texto.pack()

botao = Button(master= janelaPrincipal, text= 'Clique', command= funcClicar)
botao.pack()

janelaPrincipal.mainloop()