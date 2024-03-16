
print("Escreva um programa que ordene uma lista de strings por comprimento.\n")

def ordenar_por_comprimento(lista):
    return sorted(lista, key=len)

lista_strings = ["banana", "abacaxi", "manga", "uva", "maça", "pera",  "laranja"]
lista_ordenada = ordenar_por_comprimento(lista_strings)
print("Lista de string ordenada por comprimento", lista_ordenada)
