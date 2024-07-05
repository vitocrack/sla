def imposto(kg):
    if kg > 50:
        excesso = kg - 50
        multa = excesso * 4
        print(f"Peso de {kg}kg excede regulamentação. Multa de R${multa:.2f} aplicada.")
    else:
        print(f"Peso de {kg}kg cumpre regulamentação. Aprovado sem imposto.")
    
imposto(70)