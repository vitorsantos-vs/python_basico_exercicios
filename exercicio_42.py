print("Escreva um programa que aplique uma função a todos os itens de uma lista usando `map()`.\n")

def dobrar_num(num):
    return num * 2

lista_numeros = [1, 2, 3, 4, 5]

numeros_dobrados = list(map(dobrar_num, lista_numeros))

print(f"Números dobrados: {numeros_dobrados}")
