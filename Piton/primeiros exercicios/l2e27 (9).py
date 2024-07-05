val = float(input("Digite o valor da venda: "))

if val < 20000:
    print(f"O valor da comissão será de R${400 + val * 0.14:.2f}")
elif val < 40000:
    print(f"O valor da comissão será de R${500 + val * 0.14:.2f}")
elif val < 60000:
    print(f"O valor da comissão será de R${550 + val * 0.14:.2f}")
elif val < 80000:
    print(f"O valor da comissão será de R${600 + val * 0.14:.2f}")
elif val < 100000:
    print(f"O valor da comissão será de R${650 + val * 0.14:.2f}")
else:     
    print(f"O valor da comissão será de R${700 + val * 0.16:.2f}")