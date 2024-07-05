val = float(input("Digite o valor do carro: "))

if val < 12000:
    print(f"O valor do carro será de R${val + (val * 0.05):.2f}")
elif val < 25000:
    print(f"O valor do carro será de R${val + (val * 0.10) + (val * 0.15):.2f}")
else:     
    print(f"O valor do carro será de R${val + (val * 0.15) + (val * 0.2):.2f}")