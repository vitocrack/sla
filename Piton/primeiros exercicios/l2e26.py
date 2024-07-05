ano = int(input("Insira um ano: "))

if ano > 0:
    if (ano % 400 == 0 and ano % 4 == 0) and ano % 100 != 0:
        print(f"O ano {ano} é bissexto.")
    else:
        (f"O ano {ano} não é bissexto.")
else:
    print("Valor ínvalido.")
