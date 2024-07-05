def pot(x, y):
    for i in range(1, y + 1):
        print(f"{x} ** {i} = {x**i}")

n1, n2 = map(int, input("Digite dois número: ").split())

pot(n1, n2)
