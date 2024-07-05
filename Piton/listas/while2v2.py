a20 = int(input())
aum = 0.015
ano = 2019
while ano < 2024:
    ano += 1
    a20 = a20 + (a20 * aum)
    print("No ano de {}, seu salário foi R${:.2f}".format(ano, a20))
    aum *= 2