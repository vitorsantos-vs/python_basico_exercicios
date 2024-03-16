print("Escreva um programa que calcule o IMC (Índice de Massa Corporal).\n")

def calcular_imc(peso, altura):
    return  peso / (altura ** 2)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite uma altura: "))

imc = calcular_imc(peso, altura)

if imc < 16:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Magreza Grave'.")
elif imc >= 16 and imc < 17:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Magreza Moderada'.")
elif imc >= 17 and imc < 18.5:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Magreza Leve'.")
elif imc >= 18.5 and imc < 25:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Saudável'.")
elif imc >= 25 and imc < 30:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Sobrepeso'.")
elif imc >= 30 and imc < 35:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Obesidade Grau I'.")
elif imc >= 35 and  imc < 40:
    print(f"O seu imc é {imc:.1f} e esta na classificação de 'Obesidade Grau II'.")
else:
    print(f"O seu imc é {imc} e esta na classificação de 'Obesidade Grau III'.")
    