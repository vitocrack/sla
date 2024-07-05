n1, n2 = input("Insira dois números: ").split()
n1, n2 = int(n1), int(n2)

if n1 == n2:
    print("O dois números são iguais.")
else:
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    print("{} é maior que {}, por {} de diferença".format(maior, menor, maior - menor))