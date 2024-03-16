print("Escreva um programa que imprima todas os meses de um ano específico usando o módulo `calendar` e pandas.\n")

import calendar
import pandas as pd

# Função para criar uma lista de datas de um mês específico
def criar_lista_de_datas(ano, mes):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    data_do_mes = cal.itermonthdays(ano, mes)
    
    lista_de_datas = []
    
    for dia in data_do_mes:
        if dia != 0:
            lista_de_datas.append(f"{ano}-{mes:02d}-{dia:02d}")
    
    return lista_de_datas

# Função para imprimir os meses lado a lado como uma tabela
def imprimir_meses_lado_a_lado(ano):
    meses = []
    # Criar uma lista de datas para cada mês e adicionar à lista de meses
    for mes in range(1, 13):
        meses.append(criar_lista_de_datas(ano, mes))
    
    # Encontrar o mês com o maior número de dias para padronizar o tamanho das listas
    max_dias = max(len(mes) for mes in meses)
    
    # Padronizar o tamanho das listas adicionando strings vazias para os meses com menos dias
    for mes in meses:
        mes.extend([''] * (max_dias - len(mes)))
    
    # Criar um DataFrame com os meses como colunas
    df = pd.DataFrame(meses).transpose()
    df.columns = [calendar.month_name[i] for i in range(1, 13)]
    
    # Imprimir o DataFrame como uma tabela
    print(df)

# Exemplo de uso da função para imprimir os meses de 2024 lado a lado
imprimir_meses_lado_a_lado(2024)
