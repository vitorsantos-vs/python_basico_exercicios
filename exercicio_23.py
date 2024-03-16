print("Escreva um programa que verifique se uma palavra é um palíndromo.\n")

def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", " ").lower()
    return palavra == palavra[::-1]

palavra_usuario = input("Digite uma palavra para verificar se é um palíndromo: ")

if verificar_palindromo(palavra_usuario):
    print(f"'{palavra_usuario}' é um palíndromo.")
else:
    print(f"'{palavra_usuario}' não é um palíndromo.")
    