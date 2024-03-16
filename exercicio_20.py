print("Escreva um programa que crie um cronômetro.\n")

import time

def iniciar_cronometro():
    input("Pressione ENTRER para iniciar o cronômetro...")
    inicio = time.time()
    print("Cronômetro iniciado.")
    
    input("Pressione ENTRER para PARA o cronômetro...")
    fim = time.time()
    print("Cronômetro parado.")
    
    tempo_total = fim - inicio
    print(f"Tempo total: {tempo_total:.2f} segundos.")

iniciar_cronometro() 
    