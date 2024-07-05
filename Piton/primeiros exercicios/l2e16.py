hrs = float(input("Quantas horas trabalhadas você possui este mês?"))
money = 40.50 * hrs


if money <= 2500:
    print(f"Você deve receber R${money:.2f}")
else:
    tax = money * 0.11
    money = money - tax
    print(f"Você deve receber, descontado, R${money:.2f}.")