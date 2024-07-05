while True:
    n = int(input("Insira numero ímpar: "))
    if n % 2 == 0:
        print(f"{n} não é ímpar, tente de novo.")
    else:
        break

c = 0
while c <= n:
    if c % 2 != 0:
        print(c)
    c += 1