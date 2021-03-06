from tkinter import *

class EditBoxWindow:

    def __init__(self, parent = None):
        if parent == None:
            parent = Tk()
        self.myParent = parent

        self.top_frame = Frame(parent)

        # Criando a barra de rolagem
        scrollbar = Scrollbar(self.top_frame)
        self.editbox = Text(self.top_frame, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.editbox.yview)

        # Área do texto
        self.editbox.pack(anchor=CENTER, fill=BOTH)
        self.top_frame.pack(side=TOP)

        # Texto a procurar
        self.bottom_left_frame = Frame(parent)
        self.textfield = Entry(self.bottom_left_frame)
        self.textfield.pack(side=LEFT, fill=X, expand=1)

        # Botão Find
        buttonSearch = Button(self.bottom_left_frame, text='Find', command=self.find)
        buttonSearch.pack(side=RIGHT)
        self.bottom_left_frame.pack(side=LEFT, expand=1)
        self.bottom_right_frame = Frame(parent)

    def find(self):
        self.editbox.tag_remove('found', '1.0', END)
        s = self.textfield.get()
        if s:
            idx = '1.0'
            while True:
                idx =self.editbox.search(s, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                lastidx = '%s+%dc' % (idx, len(s))
                self.editbox.tag_add('found', idx, lastidx)
                idx = lastidx
            self.editbox.tag_config('found', foreground='red')
       
if __name__=="__main__":
    root = Tk()
    myapp = EditBoxWindow(root)