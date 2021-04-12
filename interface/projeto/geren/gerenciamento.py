from geren.datas import data_hora_atuais

def abertura():
    arquivo = open('./geren/aberturafechamento.txt', 'a')
    data =  data_hora_atuais()
    arquivo.write(f'\n---------------------------------------------------------------\n')
    arquivo.write(f'Data e hora de abertura do sistema: {data}.\n')
    arquivo.close()

def fechamento():
    arquivo = open('./geren/aberturafechamento.txt', 'a')
    data =  data_hora_atuais()
    arquivo.write(f'Data e hora de fechamento do sistema: {data}.\n')
    arquivo.write(f'---------------------------------------------------------------')
    arquivo.close()
