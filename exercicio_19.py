print("Escreva um programa que leia um arquivo de texto e imprima seu conteúdo.\n")

nome_do_arquivo = 'data_hora.txt'

try:
    with open(nome_do_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print(f"O arquivo {nome_do_arquivo} não foi encontrado.")
    