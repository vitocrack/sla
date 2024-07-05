altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / altura**2

print("Imc de",imc)
if imc < 18.5: 
    print("Abaixo do peso")
elif imc < 24.5:
    print("Saudável")
elif imc < 30:
    print("peso em excesso ")
elif imc < 35: 
    print("Obesidade grau I")
elif imc < 40:
    print("Obesidade grau II(severa)")
else:
    print("Obesidade grau III(mórbida)")