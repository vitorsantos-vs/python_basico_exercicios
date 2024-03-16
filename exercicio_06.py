print("Escreva um programa que converta graus Celsius em Fahrenheit.\n")

def celsius_para_fahrenheit(c):
    return(c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return(f - 32) * 5/9

temperatura_celsius = float(input("Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius:.1f}°C é igual a {temperatura_fahrenheit:.1f}°F")

temperatura_fahrenheit = float(input("Fahrenheit: "))
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit:.1f}°F é igual a {temperatura_celsius:.1f}°C")