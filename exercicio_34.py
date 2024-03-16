print("Escreva um programa que encontre a moda de uma lista de números.\n")

def calcular_moda(numeros):
    frequencia = {}
    for numero in numeros:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
    maxima_frequencia = max(frequencia.values())
    modas = [numero for numero, freq in frequencia.items() if freq == maxima_frequencia]
    return modas

lista_numeros = [1, 2, 2, 3, 4, 4, 4, 5, 2, 4]
moda = calcular_moda(lista_numeros)

print(f"A moda da lista é: {moda}")
