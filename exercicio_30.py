print("Escreva um programa que imprima os primeiros n números da sequência de Fibonacci.\n")

def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    while len(sequencia) < n:
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n = int(input("Quantos números da sequencia da Fibonacci você quer? "))
sequencia_fibonacci = fibonacci(n)

print(f"Os primeiros {n} da seguencia de Fibonacci são: {sequencia_fibonacci}")
