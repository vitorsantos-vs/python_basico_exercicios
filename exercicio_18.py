print("Escreva um programa que crie um arquivo de texto e salve a hora e data nele.\n")

from datetime import datetime

data_hora_atual = datetime.now()

data_hora_em_texto = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')

nome_do_arquivo = 'data_hora.txt'

with open(nome_do_arquivo, 'a') as arquivo:
    arquivo.write(data_hora_em_texto + '\n')

print(f"Data e Hora atuais salvas no arquivo {nome_do_arquivo}")
