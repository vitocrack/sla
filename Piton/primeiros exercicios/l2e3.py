n1, n2 = input("Digite dois números: ").split()
n1, n2 = int(n1), int(n2)

if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")