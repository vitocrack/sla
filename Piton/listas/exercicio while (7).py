num = int(input("Digite um valor: "))
tot = 1

for i in range(num, 0, -1):
    print(i, end='')
    tot *= i
    if i == 1:
        print(end=" = ")
    else:
        print(end=" * ")
print(tot)