print("Escreva um programa que conte o número de vogais em uma string.\n")

def contar_vogais(texto):
    vogais = 'aeiou'
    contador = sum(1 for letra in texto.lower() if letra in vogais)
    return contador

texto_usuario = input("Digite uma texto para contar  as vogais: ")
quantidade_vogais = contar_vogais(texto_usuario)

print(f"O texto '{texto_usuario}' possui {quantidade_vogais} vogais.")
