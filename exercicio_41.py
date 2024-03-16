print("Escreva um programa que filtre números pares em uma lista usando `filter()`.\n")

# Função para verificar se um número é par
def eh_par(num):
    return num % 2 == 0

# Lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar filter() para filtrar números pares
numeros_pares = list(filter(eh_par, lista_numeros))

# Imprimir os números pares
print(f"Números pares na lista: {numeros_pares}")
