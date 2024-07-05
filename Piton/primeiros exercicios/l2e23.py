mes = int(input("Digite um número de 1 a 7, cada número representa um mes da semana: "))

if 1 <= mes <= 12:
    if mes == 1:
        res = "janeiro"
    elif mes == 2:
        res = "fevereiro"
    elif mes == 3:
        res = "março"
    elif mes == 4:
        res = "abril"
    elif mes == 5:
        res = "maio"
    elif mes == 6:
        res = "junho"
    elif mes == 7:
        res = "julho"
    elif mes == 8:
        res = "agosto"
    elif mes == 9:
        res = "setembro"
    elif mes == 10:
        res = "outubro"
    elif mes == 11:
        res = "novembro"
    else:
        res = "dezembro"
    print(f"Você escolheu {res}.")
else:
    print("Valor inválido.")