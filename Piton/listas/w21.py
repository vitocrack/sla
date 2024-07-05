n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro: "))

l = [n1, n2]
menor, maior = min(l), max(l)
c = menor 
mult = []
soma = []

while c <= maior:
    if c % 2 == 0:
        mult.append(c)
    else:
        soma.append(c)
    c += 1
    
m = 1
for mul in mult:
    m *= mul
s = 0
for som in soma:
    s += som

print(f"Soma: {s}, Multiplicação: {m}")

