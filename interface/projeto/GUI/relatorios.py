try:
    from tkinter import *
except:
    from Tkinter import *

class Janela:
    def __init__(self,toplevel):        
        self.toplevel = toplevel
        self.toplevel.title('Relatórios')

        self.entregas=Frame(toplevel)
        self.entregas['background'] = '#F2F2F2'
        self.entregas.pack(expand=TRUE,anchor=NW,padx=15,pady=15)
        
        self.textentregas = Label(self.entregas, text='Relatórios de Entrega')
        self.textentregas['background'] = '#F2F2F2'
        self.textentregas['font']=('Arial','20')        
        self.textentregas['fg']='black'
        self.textentregas.pack()

        self.brelatorio=Button(self.entregas,text='Gerar relatórios de entregas por dia')
        self.brelatorio['background'] = '#2F545C'
        self.brelatorio['font']=('Arial','13')        
        self.brelatorio['fg']='#FFFFFF'
        #self.brelatorio.bind("<Button-1>", self.relatorios) #
        self.brelatorio.pack(side=LEFT)

        self.brelatorio=Button(self.entregas,text='Exibir relatórios de entregas por dia')
        self.brelatorio['background'] = '#2F545C'
        self.brelatorio['font']=('Arial','13')        
        self.brelatorio['fg']='#FFFFFF'
        #self.brelatorio.bind("<Button-1>", self.relatorios) #
        self.brelatorio.pack(side=LEFT)

        self.itens=Frame(toplevel)
        self.itens.pack(expand=TRUE,anchor=NW,padx=15,pady=15)

        self.textitens = Label(self.itens, text='Produtos e Ingredientes')
        self.textitens['background'] = '#F2F2F2'
        self.textitens['font']=('Arial','20')        
        self.textitens['fg']='black'
        self.textitens.pack()

        self.brelatorio=Button(self.itens,text='Gerar relatórios de itens e ingredientes por dia')
        self.brelatorio['background'] = '#2F545C'
        self.brelatorio['font']=('Arial','13')        
        self.brelatorio['fg']='#FFFFFF'
        #self.brelatorio.bind("<Button-1>", self.relatorios) #
        self.brelatorio.pack(side=LEFT)

        self.brelatorio=Button(self.itens,text='Exibir relatórios de itens e ingredientes por dia')
        self.brelatorio['background'] = '#2F545C'
        self.brelatorio['font']=('Arial','13')        
        self.brelatorio['fg']='#FFFFFF'
        self.brelatorio.bind("<Button-1>", self.exb_itens_dia())
        #self.brelatorio.bind("<Button-1>", self.relatorios) #
        self.brelatorio.pack(side=LEFT)

        def exb_itens_dia(self, event):
            print('\nTeste de exibição\n')
       

def relatorios():
    raiz=Tk()
    Janela(raiz)
    raiz['bg'] = '#F2F2F2'
    raiz.geometry('800x600')
    raiz.mainloop()