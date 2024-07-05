def nota_final(x, y, z, letra):
    if letra.lower() == 'a':
        nota = (x + y + z) / 3
        print(f"Nota aritmetica: {nota:.2f}")
    else:
        nota = (x + y + z) / (5 + 3 + 2)
        print(f"Nota ponderada: {nota:.2f}")
    
n1, n2, n3 = input("Digite suas 3 notas: ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)
l = input("Digite A para aritmética, e P para ponderada: ")

nota_final(n1, n2, n3, l)
