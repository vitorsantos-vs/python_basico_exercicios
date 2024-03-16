print("Escreva um programa que verifique se uma lista está vazia ou não.\n")

def verificar_lista_vazia(lista):
    return not lista

lista_teste = []

if verificar_lista_vazia(lista_teste):
    print("A lista está vazia.")
else:
    print("A lista não está vazia.")
