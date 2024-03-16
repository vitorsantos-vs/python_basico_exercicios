print("Escreva um programa que gere uma senha aleatória.\n")
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Definir o tamanho da senha desejada
tamanho_da_senha = int(input("Digite o tamanho da senha: "))

# Gerar e imprimir a senha
senha_aleatoria = gerar_senha(tamanho_da_senha)
print(senha_aleatoria)
