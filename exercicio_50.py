print("Escreva um programa que simule um jogo de pedra, papel e tesoura.\n")

import random

def jogar_pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    escolha_usuario = input("Escolha [Pedra, Papel, Tesoura]: ").lower()
    
    if escolha_usuario not in opcoes:
        print("Escolha inválida!")
        return
    
    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")
    
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura' ) or \
         (escolha_usuario == 'papel' and escolha_usuario == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        
jogar_pedra_papel_tesoura()
