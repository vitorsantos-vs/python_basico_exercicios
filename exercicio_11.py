print("Escreva um programa que converta metros para quilômetros.\n")

def metros_para_quilometros(metros):
    return metros / 1000

metros = float(input("Digite o valor em metros para converter em quilômetros: "))
quilometros = metros_para_quilometros(metros)

print(f"{metros} metros é igual a {quilometros} quilômetros.")
