n = []
print("Insira 5 números\n")
while (len(n) < 5):
    add = int(input("Digite: "))
    n.append(add)

print(f"Soma de todos os números é: {sum(n)}\nOs números inseridos foram:")
for i in n:
    print(i)
     