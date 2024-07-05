i1, i2, r1 = input("Escreva 2 numeros inteiros, e um real: ").split()
i1, i2 = int(i1), int(i2)
r1 = float(r1)

print(i1 * (i2 // 2),"\n",(i1 * 3) + r1,"\n",r1**3)