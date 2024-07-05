while True:
    n = int(input("digite um numero de 100 a 1999: "))
    if n < 100 and n > 1999:
        print("valor invalido, tente novamente")
    else:
        break

print(*list(str(n)))
