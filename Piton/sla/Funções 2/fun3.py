def val(x):
    if x > 0:
        s = 1
    elif x < 0:
        s = -1
    else:
        s = 0
    print(s)

n = int(input("Digite um numero: "))
val(n)