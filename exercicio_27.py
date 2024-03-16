print("Escreva um programa que encontre o segundo maior número em uma lista.\n")

def segundo_maior(lista):
    maior =  max(lista)
    lista.remove(maior)
    
    segundo_maior = max(lista)
    lista.append(maior)
    
    return segundo_maior

lista_numeros = [1, 2, 5, 3, 4, 6, 7]
segundo_maior_numero = segundo_maior(lista_numeros)

print(f"O segundo maior número na lsita é {segundo_maior_numero}.")
