print("Escreva um programa que encontre a mediana de uma lista de números.\n")

def calcular_mediana(numeros):
    numeros.sort()
    
    n = len(numeros)
    if n % 2 == 1:
        return numeros[n // 2]
    else:
        return (numeros[n // 2 - 1] + numeros[n // 2]) / 2
    
lista_numero = [3, 1, 4, 2, 5, 6]
mediana = calcular_mediana(lista_numero)

print(f"A mediana da lista é: {mediana}")
