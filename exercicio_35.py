print("Escreva um programa que calcule o juros simples dado capital, taxa e tempo.\n")

def calcular_juros_simples(capital, taxa, tempo):
    juros =  capital * (taxa / 100) * tempo
    return juros

capital = float(input("Dgite o valor do capital: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = int(input("Digite o tempo do investimento: "))

juros = calcular_juros_simples(capital, taxa, tempo)

print(f"O juros simples sobre o capital de {capital} com taxa de {taxa}% ao ano durante {tempo} anos é: {juros}")
