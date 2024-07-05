idade = int(input("Digite a idade: "))
contr = int(input("Digite o tempo de contribuição: "))

if idade >= 65:
    print("Está apto para aposentar")
elif contr >= 30: 
    print("Está apto para aposentar")
elif idade >= 30 and contr >= 25:
    print("Está apto para aposentar")
else:
    print("NÃO está apto para aposentar")