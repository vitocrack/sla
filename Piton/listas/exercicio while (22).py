while True:
    n = int(input("Insira numero par: "))
    if n % 2 != 0:
        print(f"{n} não é par, tente de novo.")
    else:
        break

c = 0
while c <= n:
    if c % 2 == 0:
        print(c)
    c += 1