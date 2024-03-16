print("Escreva um programa que encontre a soma de uma lista de números usando `reduce()`.\n")

from functools import reduce

def somar(x, y):
    return x + y

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = reduce(somar, lista_numeros)

print(f"A soma dos numeros da lista é: {soma}")
