# -*- coding: utf-8 -*-
# arquivo app.py
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio,Gtk,Gdk


class AppWindow(Gtk.ApplicationWindow):
    '''
        Classe responsável pela criação da janela.
        Essa é a estrutura mais básica de uma janela Python GTK.
        Ela começa herdando da classe Gtk.ApplicationWindow
    '''
    def __init__(self, app):
                '''
        No metodo init tem 2 parâmetros o primeiro é o self e o segundo é app.
        Na estrutura de orientação a objetos do python é padrão que todos 
        os metodos de uma classe tem como primeiro parâmetro o self na declaração do metodo.
        Agora o parâmetro app é a instância app que chamou a janela.
        '''
       # Gtk.Window.__init__(self, title="Gestão de compras",application=app)
        #self.set_default_size(980,600)

class App(Gtk.Application):
    '''
       Classe responsável por gerenciar a applicação e o seu ciclo de vida.
       Apartir desta classe que iniciaremos a primeira janela.
    '''
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="app.home",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

   
    def do_activate(self):
        '''
           do_activate é um metodo do ciclo de vida de aplicação e irá iniciar 
           junto com a aplicação.Aqui instânciamos AppWindow e a exibimos. 
        '''
        window = AppWindow(self)
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()    
	

if __name__ == '__main__':
    app = App()
    app.run(sys.argv)