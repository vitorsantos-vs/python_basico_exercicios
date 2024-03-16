print("Escreva um programa que verifique se um número é par ou ímpar.\n")

def verificar(num):
    if num % 2 == 0:
        return "PAR"
    elif num % 2 == 1:
        return "IMPAR"
          
numero = int(input("Digite um número: "))
resultado = verificar(numero)

print(f"O numero {numero} é {resultado}.")
