print("Escreva um programa que converta números romanos em números inteiros.\n")

def romano_para_inteiro(s):
    romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    valor_inteiro = 0
    valor_anterior = 0
    
    for caractere in s[::-1]:
        valor_atual = romanos[caractere]
        if valor_atual < valor_anterior:
            valor_inteiro -= valor_atual
        else:
            valor_inteiro +=  valor_atual
            
    return valor_inteiro

numeral_romano = "MMI"
valor_inteiro = romano_para_inteiro(numeral_romano)

print(f"O valor inteiro do numeral romano {numeral_romano} é {valor_inteiro}")
