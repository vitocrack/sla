main, par, imp = [], [], []
c = 0
while c < 20:
    n = int(input("insira numero: "))
    main.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    c += 1
print(f"Pares:{par}\nImpares:{imp}")