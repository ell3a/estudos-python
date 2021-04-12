from datetime import date
from datetime import datetime

def data_hora_atuais():
    data_hora_sistema = datetime.now()
    data_hora = data_hora_sistema.strftime('%d/%m/%Y às %H:%M')
    return data_hora

def data_atual():
    data_atual = date.today()    
    data = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
    return data

def numero_pedido():
    data_atual = date.today()
    ano = str(data_atual.year%1000)
    data_hora_sistema = datetime.now()
    tmp = data_hora_sistema.strftime('%m%d%H%M')
    numero_pedido = f'{ano}{tmp}'
    return numero_pedido