gas = float(input("Digite a quantidade de gasolina consumida em litros: "))
km = float(input("Digite a quilometragem andada com essa quantidade de gasolina: "))

eco = km / gas

if eco < 8:
    print(f"Seu carro faz {eco:.1f}km/l, tá bebendo em")
elif eco < 14: 
    print(f"Seu carro faz {eco:.1f}km/l, econômico")
else:
    print(f"Seu carro faz {eco:.1f}km/l, SUPER econômico")