val = float(input("Digite o valor antigo: "))

if val < 50:
    print(f"O valor atualizado é de R${val * 1.05:.2f}")
elif val < 100:
    print(f"O valor atualizado é de R${val * 1.10:.2f}")
else: 
    print(f"O valor atualizado é de R${val * 1.15:.2f}")