l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

lados = [l1, l2, l3]
lados.sort()

if lados[0] + lados[1] >= lados[2]:
    print("Este triângulo é válido")
    if (lados[0] == lados[1] or lados[1] == lados[2]) and not(lados[0] == lados[1] == lados[2]):
        print("O triângulo é isoceles")
    elif lados[0] == lados[1] == lados[2]:
        print("O triângulo é equilátero")
    else:
        print("O triângulo é escaleno")
else:
    print("Este triângulo é inválido")