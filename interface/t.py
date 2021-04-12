from tkinter import Tk
from tkinter import Menu
from tkinter import ttk
from types import SimpleNamespace


def gui(root):
    #INICIA JANELA
    root.geometry('800x433')
    root.option_add('*tearOff', False)
    root.title('Gerenciamento de Estoque')

    #INICIA BARRA DE MENUS
    menuBar = Menu(root)
    menuFile = Menu(menuBar)
    menuFile.add_command(label = 'Checar agora', command = None)
    menuFile.add_command(label = 'Sair', command = None)
    menuBar.add_cascade(menu = menuFile, label = 'Opções')
    root.config(menu = menuBar)
    
    #INICIA ABAS
    tabControl = ttk.Notebook(root)
    aba1 = ttk.Frame(tabControl)
    aba2 = ttk.Frame(tabControl)
    tabControl.add(aba1, text = 'Cadastrar Pedido')
    tabControl.add(aba2, text = 'Relatórios')
    tabControl.pack(expand = 1, fill = 'both')    

def sair():
    exit()

    
    return SimpleNamespace() #falta adicionar componentes


if __name__ == '__main__':
    root = Tk()
    guiref = gui(root)
    root.mainloop()