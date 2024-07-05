notat, notaa, notae = input("Digite, respectivamente, a nota sua nota em Trabalho em Laboratório, Avaliação semestral e Exame Final: ").split()
notat, notaa, notae = float(notat), float(notaa), float(notae)

if (10 >= notat >= 0) and (10 >= notaa >= 0) and (10 >= notae >= 0):
    media = (notat * 2 + notaa * 3 + notae * 5) // 10
    if 5.9 >= media >= 3:
        print(f"Sua média é {media}, você ficou de recuperação.")
    elif 10 >= media >= 6:
        print(f"Sua média é {media}, você foi aprovado.")
    else:
        print(f"Sua média é {media}, você foi reprovado.")
else:
    print("Erro: Um dos valores inseridos é inválido.")