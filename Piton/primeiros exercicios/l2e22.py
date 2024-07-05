dia = int(input("Digite um número de 1 a 7, cada número representa um dia da semana: "))

if 1 <= dia <= 7:
    if dia == 1:
        res = "domingo"
    elif dia == 2:
        res = "segunda-feira"
    elif dia == 3:
        res = "terça-feira"
    elif dia == 4:
        res = "quarta-feira"
    elif dia == 5:
        res = "quinta-feira"
    elif dia == 6:
        res = "sexta-feira"
    else:
        res = "sábado"
    print(f"Você escolheu {res}.")
else:
    print("Valor inválido.")