c = 0
l =[]
print("Insira 10 valores.\n")

while c < 10:
    l.append(int(input("valor: ")))
    c += 1

print(sum(l))