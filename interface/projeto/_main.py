try:
    from tkinter import *
except:
    from Tkinter import *

import geren.gerenciamento as ger
import GUI.cadastro as cad
import GUI.sobre as sob
import GUI.relatorios as rel

ger.abertura()

class Janela:

    def __init__(self,toplevel):

        self.toplevel = toplevel
        self.toplevel.title('Gerenciamento de Pedidos')

        self.topo=Frame(toplevel)
        self.cent=Frame(toplevel)
        self.base=Frame(toplevel)
        self.topo.pack(expand=TRUE,anchor=NW,padx=15,pady=15)
        self.cent.pack(expand=TRUE,anchor=W,padx=15,pady=15)
        self.base.pack(expand=TRUE,anchor=SE,padx=15,pady=15)

        # BOTÃO RELATÓRIO
        self.brelatorio=Button(self.topo,text='Relatórios')
        self.brelatorio['background'] = '#2F545C'
        self.brelatorio['font']=('Arial','15')        
        self.brelatorio['fg']='#FFFFFF'
        self.brelatorio.bind("<Button-1>", self.relatorios) #
        self.brelatorio.pack(side=LEFT)

        # BOTÃO SOBRE
        self.bsobre=Button(self.topo,text='?')
        self.bsobre['background'] = '#C5D1CF'
        self.bsobre['font']=('Arial','15')        
        self.bsobre['fg']='black'
        self.bsobre.bind("<Button-1>", self.sobre)
        self.bsobre.pack(side=LEFT)

        # BOTÃO CADASTRAR PEDIDO
        self.bcadastrar=Button(self.cent,text='Cadastrar Pedido')
        self.bcadastrar.bind("<Button-1>", self.cadastrar)
        self.bcadastrar['background'] = '#2F545C'
        self.bcadastrar['font']=('Arial','30')
        self.bcadastrar['fg']='#FFFFFF'
        self.bcadastrar['width']=15
        self.bcadastrar['height']=1
        self.bcadastrar.pack()

        # BOTÃO SAIR
        self.bsair=Button(self.base,text='Sair')
        self.bsair['background'] = '#C5D1CF'
        self.bsair['font']=('Arial','15')        
        self.bsair['fg']='black'
        self.bsair.bind("<Button-1>", self.sair)
        self.bsair.pack(side=LEFT)

    def sair(self, event):
        ger.fechamento()
        sys.exit()

    def sobre(self, event):
        sob.sobre()

    def cadastrar(self, event):
        cad.cadastrar()

    def relatorios(self, event):
        rel.relatorios()


raiz=Tk()
# Para alterar a cor da janela
raiz['bg'] = '#F2F2F2'
Janela(raiz)
raiz.geometry('750x450')
raiz.mainloop()