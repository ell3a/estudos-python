from tkinter import *

class Janela:

    def __init__(self,top_level):

        self.topo=Frame(top_level)
        self.cent=Frame(top_level)
        self.base=Frame(top_level)
        self.topo.pack()
        self.cent.pack()
        self.base.pack()

        self.brelatorio=Button(self.topo,text='Relatórios')
        self.brelatorio.pack(side=LEFT)

        self.bsobre=Button(self.topo,text='?')
        self.bsobre.pack(side=LEFT)

        self.bcadastrar=Button(self.cent,text='Cadastrar')
        self.bcadastrar.pack()

        self.bsair=Button(self.base,text='Sair')
        self.bsair.pack(side=RIGHT)

raiz=Tk()
Janela(raiz)
raiz.mainloop()