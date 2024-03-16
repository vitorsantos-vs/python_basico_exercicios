print("Escreva um programa que remova itens duplicados de uma lista.\n")

def remove_duplicados(lista):
    return list(set(lista))

lista_com_duplicados = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9, 9, 10]
lista_sem_duplicados = remove_duplicados(lista_com_duplicados)

print(f"Lista original: {lista_com_duplicados}")
print(f"Lista sem duplicados: {lista_sem_duplicados}")
