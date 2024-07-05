val = float(input("Digite o valor do produto: "))
est = input("Digite o Estado final: ").upper()


if est == "MG":
    print(f"O valor final é de R${val * 1.07:.2f}")
elif est == "SP":
    print(f"O valor final é de R${val * 1.12:.2f}")
elif est == "RJ":
    print(f"O valor final é de R${val * 1.15:.2f}")
elif est == "MS":
    print(f"O valor final é de R${val * 1.08:.2f}")
else:
    print("O valor inserido não é válido")