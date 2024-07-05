def vol(x, y):
    v = 3.141592 * x * y
    print(f"{v:.2f}")
raio, altura = input("Digite raio e altura: ").split()
raio, altura = int(raio), int(altura)

vol(raio, altura)