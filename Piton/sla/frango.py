n = True
while n:
    num = int(input("Digite um número de 0 a 9"))
    if num != 7:
        print("Errou.")
    elif num > 9:
        print(f"É de 0 a 9! {num} não se encaixa entre esses dois números.")
    else:
        print("Acertou.")
        n = False

print("\nParabéns! Agora digite outro numero.")

n = True
while n:
    num2 = int(input("Digite um número de 0 a 20\n"))
    if num2 != 14:
        print("Errou.")
    elif num2 > 20:
        print("De 0 a 20, eu falei! Tente de novo.")
    else:
        print("Acertou")
        n = False

print("Parabéns, última fase agora.")

n = True
while n:
    num3 = int(input("Digite agora um número entre 0 a 50\n"))
    if num3 != 34:
        print("Errou! Tente de novo.")
    elif num3 > 50:
        print("De 0 a 50, lembre-se. Tente novamente.")
    else:
        print("Parabéns, você ganhou!")
        n = False