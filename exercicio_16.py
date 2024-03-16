print("Escreva um programa que calcule o MDC (Máximo Divisor Comum).\n")

def mdc(a, b):
    while b  != 0:
        a, b = b, a % b
    return a

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f"O MDC de {numero1} e {numero2} é {mdc(numero1, numero2)}")
