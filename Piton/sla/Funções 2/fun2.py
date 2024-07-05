def tempo(d, m, a):
    if m[0] == "0":
        m = m[1:]
    m = int(m)
        
    meses = ["INVALIDO", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    print(f"Dia {d} de {meses[m]} de {a}.")

dia, mes, ano = input("Digite uma data (dd/mm/aa): ").split('/')
tempo(dia, mes, ano)