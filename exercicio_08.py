print("Escreva um programa que encontre o fatorial de um número.\n")

def fatoral(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

num =  int(input("Digite um número para calcular o fatoral: "))
resultado = fatoral(num)
print(f"O fatoral de {num} é {resultado}.")
