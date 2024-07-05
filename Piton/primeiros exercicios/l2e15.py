prova1, prova2 = input("Digite a nota da prova 1 e prova 2:").split()
prova1, prova2 = float(prova1), float(prova2)
if (prova1 <= 10 and prova1 >= 0) and (prova2 <= 10 and prova2 >= 0):
    media = (prova1 + prova2) // 2
    print(f"Sua média é {media}.")
else:
    print("ERRO: VALOR ÍNVALIDO")