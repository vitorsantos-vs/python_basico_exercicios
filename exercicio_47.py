print("Escreva um programa que verifique se um ano é bissexto.\n")

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
ano = int(input("Digite um ano: "))
if ano_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano nissexto.")
    