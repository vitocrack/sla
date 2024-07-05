c = 0
l =[]
print("Insira 10 valores.\n")

while c < 10:
    n = int(input("valor: "))
    if n >= 0:
            l.append(n)
    c += 1

print(sum(l)//len(l))