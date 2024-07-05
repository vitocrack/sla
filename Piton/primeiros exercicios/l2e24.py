bsmenor, bsmaior, alt = input("Insira a base menor, a base maior e altura do trápézio: ").split()
bsmenor, bsmaior, alt = int(bsmenor), int(bsmaior), int(alt)

print("A área do trapézio é {}".format((((bsmenor + bsmaior) * alt)// 2)))