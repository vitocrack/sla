sr, emp = input("Digite seu sálario e valor de prestação de empréstimo: ").split()
sr, emp = float(sr), float(emp)

if ((emp // sr - 1) * 100) > 20:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
