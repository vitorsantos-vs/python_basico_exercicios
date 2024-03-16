print("Escreva um programa que converta uma string em uma lista de palavras.\n")

def converter_string_em_lista(texto):
    lista_de_palavras = texto.split()
    return lista_de_palavras

texto_usuario = input("Digite uma frase: ")
lista_de_palavras = converter_string_em_lista(texto_usuario)

print(f"A lista de palavras é {lista_de_palavras}")
