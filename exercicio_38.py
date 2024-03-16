print("Escreva um programa que desenhe um quadrado usando o módulo `turtle`.\n")

import turtle

def desenha_quadrado(tamanho_do_lado):
    for _ in range(4):
        turtle.forward(tamanho_do_lado)
        turtle.right(90)
        
tamanho_do_lado = 200
turtle.speed(1)
desenha_quadrado(tamanho_do_lado)

turtle.done()  
