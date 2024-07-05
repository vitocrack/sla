while True:
    n = int(input("Insira numero par: "))
    if n % 2 != 0:
        print(f"{n} não é par, tente de novo.")
    else:
        break

c = n
while c >= 0:
    if c % 2 == 0:
        print(c)
    c -= 1