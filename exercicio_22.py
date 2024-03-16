print("Escreva um programa que multiplique todos os números de uma lista.\n")

def mult_lista(lista, mult):
    return [item * mult for item in lista]

lista = []
for i in range(5): 
    numero = int(input(f"Digite o número {i+1} da lista: "))
    lista.append(numero)

mult = int(input("Digite o multiplicador: "))

lista_final = mult_lista(lista, mult)

print(f"A lista original é {lista}.")
print(f"A lista após a multiplicação é {lista_final}.")

