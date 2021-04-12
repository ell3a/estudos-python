import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Teste de Janela')
        
        self.lbl = tk.Label(self.janela, text =    'Leandro Vieira', background='red')
        self.lbl['font'] = ('Verdada', '16')
        self.lbl.pack(pady = 20)
        
        self.lbl2 = tk.Label(self.janela, text =    'Leandro Vieira', background='blue')
        self.lbl2['font'] = ('Verdada', '16')
        self.lbl2.pack(ipady = 25, ipadx = 10)

# Instância de Tk
# Gera a interface, uma janela
# Componente de uma interface Widgets
raiz = tk.Tk()

Tela(raiz)
raiz.mainloop()