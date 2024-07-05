v1 = float(input("Digite o primeiro valor: "))
mat = input("O que será feita com esse valor? \n[A,S,M,D] ").upper()
v2 = float(input("Digite o primeiro valor: "))

if mat == "A":
    print(f"{v1} + {v2} = {v1 + v2}")
elif mat == "S":
    print(f"{v1} - {v2} = {v1 - v2}")
elif mat == "M":
    print(f"{v1} x {v2} = {v1 * v2}")
elif mat == "D":
    print(f"{v1} / {v2} = {v1 / v2}")
else:
    print("Valor inválido")