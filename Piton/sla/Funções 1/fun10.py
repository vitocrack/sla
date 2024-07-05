def compra(carro,entrada,juros,parcelas):
    en = carro * (entrada / 100)
    print(en)
    carro = (carro - en) + carro * (juros / 100 )
    v_parcelas = carro / 12
    print(f"Valor da entrada: R${en:.2f}\nValor do carro com juros: R${carro:.2f}\nValor de cada uma das {parcelas} parcelas: R${v_parcelas:.2f}")

compra(24000,20,3,12)