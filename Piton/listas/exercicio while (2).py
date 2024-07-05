notas = []
while True:
    nota = float(input("Digite uma nota válida: "))
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        break
print("A média das notas foi ", sum(notas) / len(notas))