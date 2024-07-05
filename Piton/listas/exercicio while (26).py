qnt = int(input("Quantos numeros deseja digitar: "))
n = []
c = 0

while c < qnt:
    sla = int(input("digite numero: "))
    n.append(sla)
    c += 1
print(max(n))
