val = float(input("Digite o valor da hora de trabalho: ")) 
hor = float(input("Digite a quantidade de horas trabalhadas: "))

sal_brt = val * hor
ir = sal_brt * 0.11
inss = sal_brt * 0.08
sind = sal_brt * 0.05
sal_liq = sal_brt - ir - inss - sind


print(f"O salário bruto foi de R${sal_brt:.2f}")
print(f"O desconto de imposto de renda foi de R${ir:.2f}")
print(f"O desconto do INSS foi de R${inss:.2f}")
print(f"O desconto do sindicato foi de R${sind:.2f}")
print(f"O salário bruto foi de R${sal_liq:.2f}")