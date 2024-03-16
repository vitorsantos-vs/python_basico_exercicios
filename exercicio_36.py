print("Escreva um programa que calcule o juros composto dado capital, taxa, tempo e frequência de capitalização.\n")

def calcular_juros_composto(capital, taxa, tempo, frequencia):
    taxa_por_periodo = taxa / (frequencia * 100)
    total_periodos = tempo * frequencia
    montante = capital * (1 + taxa_por_periodo) ** total_periodos
    juros_composto = montante - capital
    return juros_composto

capital = float(input("Digite o valor do capital: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = int(input("Digite o tempo da aplicação: "))
frequencia = int(input("Digite a  frequência: "))

juros = calcular_juros_composto(capital, taxa, tempo, frequencia)

print(f"O juros composto sobre o capital de {capital} com a taxa de {taxa}% ao ano durente {tempo} anos e frequencia de capitalização trimetral é {juros:.2f}")    
