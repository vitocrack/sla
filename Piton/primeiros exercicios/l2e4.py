n1, n2, n3 = input("Digite um número: ").split()
n1 , n2, n3 = int(n1), int(n2), int(n3)

if n1 < n2 < n3:
    print(f"{n1}, {n2}, {n3}. Você inseriu números em ordem crescente.")
else:
    print(f"{n1}, {n2}, {n3}. Você não inseriu números em ordem crescente.")

