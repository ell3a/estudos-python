#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
Calculadora com GUI em Tkinter, utilizando funções internas do Python
Baseada na implementação de Mark Lutz em "Programming Python", pág. 675

Autor deste script: Jean-Guy Schneider <schneidr@iam.unibe.ch>
Última modificação Mon Jun 22 17:36:02 MET DST 1998
"""
from tkinter import *

class CalcGUI (Frame):
    """
    class 'CalcGUI': a simple calculator
    """
    
    def __init__ (self, master=None):
        Frame.__init__ (self, master)
        self.pack (expand=YES, fill=BOTH)
        self.master.title ('Python Calculator')
        self.master.iconname ("pcalc")

        self._names = {}                  # private namespace for expressions

        self._text = Text (self, width=16, height=1)     # a text widget
        self._text.pack (expand=YES, fill=X)             # as display

        rows = ["abcd", "0123", "4567", "89()"]          # buttons
        for row in rows:
            frm = Frame (self)                           # into separate frame
            for char in row:
                but = Button (frm, text=char,
                              command=lambda s=self, y=char: s._append (y))
                but.pack (side=LEFT, expand=YES, fill=X)
            frm.pack (expand=YES, fill=X)

        frm2 = Frame (self)
        for char in "+-*/=":                             # operators
            but = Button (frm2, text=char,
                          command=lambda s=self, y=char: s._append (' '+y+' '))
            but.pack (side=LEFT, expand=YES, fill=X)
        frm2.pack (expand=YES, fill=X)

        frm3 = Frame (self)                               # command buttons
        but = Button (frm3, text='eval', command=lambda s=self: s.eval ())
        but.pack (side=LEFT, expand=YES, fill=X)
        but = Button (frm3, text='clear', command=lambda s=self: s._clear ())
        but.pack (side=LEFT, expand=YES, fill=X)
        but = Button (frm3, text='exit', command=self.quit)
        but.pack (side=LEFT, expand=YES, fill=X)
        frm3.pack (expand=YES, fill=X)

    def eval (self):
        try:
            cont = self._get()                           # get contents
            self._clear()                                # clear text widget
                                                         # eval as expression
            self._append('eval (cont, self._names, self._names)')
        except SyntaxError:
            try:
                exec (cont, self._names, self._names)    # exec as statement
            except:
                self._append ("ERROR")
            else:
                self._clear()                            # worked as statement
        except:
            self._append ("ERROR")                       # other errors

    # private helper functions: text widget manipulation
    def _clear (self):
        """Clear text widget"""
        self._text.delete ('1.0', '2.0')

    def _append (self, text):
        """Append 'text' to text widget"""
        self._text.insert ('1.end', text)

    def _get (self):
        """get contents of text widget"""
        return self._text.get ('1.0', '1.end')

if __name__ == '__main__':
    CalcGUI().mainloop()