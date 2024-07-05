sexo, altura = input("Digite seu sexo e sua altura: ").split()
altura = float(altura)

if sexo.lower() == "masculino":
    peso = 72.7 * altura - 58
    print(f"{peso} é seu peso ideal.")
elif sexo.lower() == "feminino":
    peso = 62.1 * altura - 44.7
    print(f"{peso} é seu peso ideal.")
else:
    print("Sexo inválido")