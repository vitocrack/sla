cod = int(input("Digite o código do lanche: "))
qtd = int(input("Digite a quantidade desse lanche a ser comprada: "))

if cod == 100:
    print(f"{qtd} unidades de Hot Dog sairá por R${12 * qtd:.2f}")
elif cod == 102:
    print(f"{qtd} unidades de X-Salada sairá por R${18.5 * qtd:.2f}")
elif cod == 103:
    print(f"{qtd} unidades de X-BACON sairá por R${25.5 * qtd:.2f}")
elif cod == 104:
    print(f"{qtd} unidades de x-Burguer sairá por R${17 * qtd:.2f}")
elif cod == 105:
    print(f"{qtd} unidades de Suco de Laranja sairá por R${9.5 * qtd:.2f}")
elif cod == 106:
    print(f"{qtd} unidades de Refrigerante sairá por R${6 * qtd:.2f}")
else:
    print("Código inválido")
