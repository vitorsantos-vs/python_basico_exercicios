print("Escreva um programa que encontre números primos até n.\n")

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos(n):
    primos = []
    for num in range(2, n+1):
        if eh_primo(num):
            primos.append(num)
    return primos

n = int(input("Encontre números primos até o número: "))
primos_encontrados = encontrar_primos(n)
print(f"Números primos até {n}:", primos_encontrados)
