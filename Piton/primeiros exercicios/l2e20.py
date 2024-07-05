n1, n2 ,n3 = input("Digite a nota das três provas: ").split()
n1, n2 ,n3 = int(n1), int(n2), int(n3)
media = (n1 * 1 + n2 * 1 + n3 * 2) //4

if media >= 60:
    print(f"Aprovado, parabéns. Sua média é {media}")
else:
    print(f"Reprovado. Sua média é {media}")