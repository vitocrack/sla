def tabela():
    c = 1.99
    for i in range(1, 51):
        print(f"{i} - R${c:.2f}")
        c += 1.99

print("Loja Quase Dois - Tabela De Preços\n")
tabela()