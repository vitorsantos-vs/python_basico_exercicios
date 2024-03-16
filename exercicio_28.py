print("Escreva um programa que combine duas listas e ordene o resultado.\n")

def combina_e_ordenar(lista1, lista2):
    lista_cobinada = lista1 + lista2
    
    lista_cobinada.sort()
    
    return lista_cobinada

lista1 = [1, 2, 3, 5 ,4]
lista2 = [6, 7, 9, 5, 8]

lista_ordenada = combina_e_ordenar(lista1, lista2)

print(f"A lista combinada e ordenada é: {lista_ordenada}")
