c = 0
p = 0
while True:
    n = int(input("Digita um numero (0 pra finalizar): "))
    c += 1
    if n % 2 == 0:
        valor = "par"
        p += 1
    elif n == 0:
        break
    else:
        valor = "ímpar"
    print(f"{n} é {valor}.\n{c} números inseridos até agora. {p} eram pares.")
