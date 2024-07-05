a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b ** 2)  - (4 * a * c)

r1 = (-b - delta**0.5) / 2*a
r2 = (-b + delta**0.5) / 2*a

#print(delta)
#print(f"{r1:.3f}")
#print(f"{r2:.3f}")

if a <= 0:
    print("Esta não é uma equação do segundo grau")
elif delta < 0:
    print("não exitem raízes para esta equação")
elif delta == 0:
    print(f"A única raiz desta função é {r1:.2f}")
elif delta > 0:
    print(f"As raízes desta função são: \n  x1 = {r1:.2f}\n  x2 = {r2:.2f}")