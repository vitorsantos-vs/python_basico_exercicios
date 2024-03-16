print("Escreva um programa que encontre o dia da semana de uma data específica.\n")

import datetime

def dia_da_semanda(ano, mes, dia):
    data = datetime.date(ano, mes, dia)
    dia_semana = data.strftime("%A")
    return dia_semana

ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))

dia_da_semana_especifico = dia_da_semanda(ano, mes, dia)

print(f"O dia da semana para {ano}-{mes}-{dia} é: {dia_da_semana_especifico}.")
print("""
Monday: Segunda-feira
Tuesday: Terça-feira
Wednesday: Quarta-feira
Thursday: Quinta-feira
Friday: Sexta-feira
Saturday: Sábado
Sunday: Domingo
      """)
