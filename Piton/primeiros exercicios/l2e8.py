n = int(input("Insira um número positivo: "))

if n < 0:
    print("ERRO: NÚMERO ÍNVALIDO.")
else:
    print("A raiz quadrada de {} é {}".format(n, n ** 0.5))