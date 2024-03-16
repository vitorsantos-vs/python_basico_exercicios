print("Escreva um programa que resolva uma equação quadrática.\n")

a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("Esta equção não possui raízes reais.")
elif D == 0:
    X = - b / (2 * a)
    print(f"Esta equeção possui uma raíz real: {X}")
else:
    X1 = (- b + D ** 0.5) / (2 * a)
    X2 = (- b - D ** 0.5) / (2 * a)
    print(f"Esta equação possui duas raízes reais: {X1} e {X2}.")
    