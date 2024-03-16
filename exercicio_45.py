print("Escreva um programa que troque as chaves pelos valores em um dicionário.\n")

dicionario_original = {'a' : 1, 'b' : 2, 'c' : 3}

dicionario_trocado = {valor: chave for chave, valor in dicionario_original.items()}

print(f"Dicionario original: {dicionario_original}")
print(f"Dicionario com chave e valor trocados: {dicionario_trocado}")
