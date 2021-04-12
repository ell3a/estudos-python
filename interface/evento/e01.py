import tkinter as tk
from tkinter import messagebox

class Tela:

    def __init__(self, master):
        self.tela = master
        self.lbl = tk.Label(self.tela, text='Abrir caixa', font=('Verdada', '16'), relief= 'raised')
        self.lbl.pack(pady=20)

        self.lbl.bind('<Button-1>',self.reposta)
    
    def reposta(self, event):
        print(event.x, event.y)
        messagebox.showinfo('Caixa de mensagem', 'Isso é uma Mensagem')
    

raiz = tk.Tk()

Tela(raiz)
raiz.mainloop()