turno = input("Insira o seu turno em M, V ou N: ")

if turno.lower() == "m":
    print("Bom dia.")
elif turno.lower() == "v":
    print("Boa tarde.")
elif turno.lower() == "n":
    print("Boa noite.")
else:
    print("Turno ínvalido.")