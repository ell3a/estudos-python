try:
    from tkinter import *
except:
    from Tkinter import *

import geren.informacoes as info

class Janela:

    def __init__(self,toplevel):

        self.toplevel = toplevel
        self.toplevel.title('Sobre')

        self.topo=Frame(toplevel)
        self.cent=Frame(toplevel)
        self.base=Frame(toplevel)
        
        self.topo.pack()
        self.cent.pack()
        self.base.pack()

        self.titulo=Label(self.topo, text='Iformações sobre a Aplicação')
        self.titulo['font']=('Verdana','18')
        self.titulo.pack()

        self.texto=Label(self.cent, text=f'{info.texto}')
        self.texto['font']=('Verdana','15')
        self.texto.pack()

def sobre():
    s=Tk()
    Janela(s)
    s.geometry('600x400')
    s.mainloop()