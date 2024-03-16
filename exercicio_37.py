print("Escreva um programa que some todos os números de uma lista.\n")

def somar_lista(lista):
    return sum(lista)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_somada = somar_lista(lista_numeros)

print(f"A soma da lista é: {lista_somada}")
