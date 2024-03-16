print("Escreva um programa que inverta uma string.\n")

def inverter_string(string):
    return string[::-1]

string_original = input("Digite uma String: " )
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
