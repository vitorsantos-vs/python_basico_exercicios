print("Escreva um programa que crie um dicionário e imprima seus itens.\n")

dicionario = {
    'nome' : 'Vitor',
    'idade' : 23,
    'profissao' : 'Data enginner',
    'cidade' : 'São Paulo'
}

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
