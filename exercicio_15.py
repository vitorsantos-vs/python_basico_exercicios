print("Escreva um programa que simule um lançamento de dados.\n")

import random

def lancar_dados():
    resultado = random.randint(1, 6)
    return resultado

print(f"O dado deu {lancar_dados()}")
