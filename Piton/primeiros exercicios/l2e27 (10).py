sal = float(input("Digite o salário do funcionário: "))
cont = int(input("Digite o tempo de contribuíção: "))

saln = 0

if sal < 500:
    saln = sal * 1.25
elif sal < 1000:
    saln = sal * 1.20
elif sal < 1500:
    saln = sal * 1.15
elif sal < 2000: 
    saln = sal * 1.10
else: 
    saln = sal


if 1 < cont < 3:
    saln += 100
elif cont < 6:
    saln += 200
elif cont < 10:
    saln += 300
else: 
    saln += 500

if saln != sal:
    print(f"O novo salário é de R${saln:.2f}")
else:
    print("Não houve alterações")