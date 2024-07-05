pro = float(input("Insira valor de produto: "))

if pro < 50:
    val = pro * 0.45
    print("O produto será vendido por R${:.2f}".format(pro + val))
else:
    print(f"O produto será vendido por R${pro:.2f}")