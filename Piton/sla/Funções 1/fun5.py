def ICMS(custo, taxa):
    imposto = (custo * (taxa / 100)) + custo
    print(imposto)

x, y = input("Digite o custo e a taxa de imposto: ").split()
x, y = int(x), int(y)

ICMS(x, y)