print("Escreva um programa que encontre todos os pares em uma lista de números.\n")

def encontrar_pares(lista):
    pares = [numero for numero in lista if numero % 2 == 0]
    return pares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
numero_pares = encontrar_pares(lista_numeros)

print(f"Os números pares na lista são: {numero_pares}")
