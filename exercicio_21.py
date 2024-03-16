print("Escreva um programa que converta segundos em horas, minutos e segundos.\n")

def converter_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes
    
total_segundos = int(input("Digite os segundos: "))
horas, minutos, segundos = converter_segundos(total_segundos)

print(f"{total_segundos} segundos é equivalente a {horas} horas, {minutos} minutos, {segundos} segundos")
