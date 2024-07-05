n = int(input("Digite número: "))

if n > 0:
    print("O valor ao cubo de {} é {}\nA raiz quadrada de {} é {}".format(n, n ** 3, n, int(n ** 0.5)))
else:
    print("ERRO NUMERO INVALIDO")