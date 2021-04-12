from tkinter import *

class Janela:
    def __init__(self,toplevel):

        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.fr2 = Frame(toplevel)
        self.fr2.pack()
        self.fr3 = Frame(toplevel)
        self.fr3.pack()

        self.botao11 = Button(self.fr1,text='Relatórios')
        self.botao11['background'] = 'green'
        self.botao11['font']=('Verdana','15')
        self.botao11.pack()

        self.botao12 = Button(self.fr1,text='?')
        self.botao12['background'] = 'green'
        self.botao12['font']=('Verdana','15')
        self.botao12.pack()

        self.botao21 = Button(self.fr2,text='Cadastrar')
        self.botao21['background'] = '#C5D1CF'
        self.botao21['font']=('Verdana','30')
        self.botao21['fg']='black'
        self.botao21['width']=20
        self.botao21['height']=2
        self.botao21.pack()

        self.botao31 = Button(self.fr3,text='Sair')
        self.botao31['background'] = 'green'
        self.botao31['font']=('Verdana','15')
        self.botao31['width']=7
        self.botao31['height']=2
        self.botao31.pack(side=RIGHT)


        '''
        self.botao1 = Button(self.fr1,text='Oi!')
        self.botao1['background']='green'
        self.botao1['font']=('Verdana','12','italic','bold')
        self.botao1['height']=3
        self.botao1.pack()
        self.botao2 = Button(self.fr1,bg='red', font=('Times','16'))
        self.botao2['text']='Tchau!'
        self.botao2['fg']='yellow'
        self.botao2['width']=12
        self.botao2.pack()
        '''

raiz=Tk()
Janela(raiz)
raiz.mainloop()