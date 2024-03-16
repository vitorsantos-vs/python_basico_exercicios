print("Escreva um programa que simule uma calculadora simples.\n")

def soma(num1, num2):
    return num1 + num2 

def subtracao(num1, num2):
    return num1 - num2

def  multiplicacao(num1, num2):
    return num1 *  num2    

def divisao(num1, num2):
    if num1 and num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero não é possível"

num1 = float(input("Digite o primeiro número: "))
num2 =  float(input("Digite o segundo número: "))

opcao = input("\nEscolha a operação desejada:\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n: ").strip()

if opcao  == '1':
    resultado = soma(num1, num2)
    print(f"A soma de {num1} e {num2} é {resultado}.")
elif opcao == '2':
    resultado = subtracao(num1, num2)
    print(f"A subtração de {num1} e {num2} é {resultado}.")   
elif opcao == '3':
    resultado = multiplicacao(num1, num2)
    print(f"A multiplicação de {num1} e {num2} é {resultado}.")
elif opcao == '4':
    resultado = divisao(num1, num2)
    print(f"A divisão de {num1} e {num2} é {resultado}.")
else:
    print("Opção inválida.")
    