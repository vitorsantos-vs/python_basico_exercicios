print("Escreva um programa que calcule a média de uma lista de números.\n")

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

lista_numero = [10, 20, 30, 40, 50, 60]
media_lista = calcular_media(lista_numero)

print(f"A média da lista é: {media_lista}")
