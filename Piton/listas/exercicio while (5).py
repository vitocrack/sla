idades = []
while True:
    idade = float(input("Digite uma idade válida: "))
    if idade >= 0:
        idades.append(idade)
    else:
        break
print("A média das idades foi ", sum(idades) / len(idades))