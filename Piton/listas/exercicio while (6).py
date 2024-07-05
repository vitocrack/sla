base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))

tot = 1
for i in range(expoente):
    tot *= base

print(tot)