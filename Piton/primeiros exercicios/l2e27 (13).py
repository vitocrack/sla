from math import ceil

alt = float(input("Digite a altura da parede a ser pintada: "))
bas = float(input("Digite a base da parede a ser pintada: "))

area = (alt * bas) * 1.1


print(f"Será necessário {ceil(area/18):.0f} galões de 18 litros, que sairá por R${ceil(area/18) * 80:.2f}")
print("Ou")
print(f"Será necessário {ceil(area/3.6):.0f} galões de 3.6 litros, que sairá por R${ceil(area/3.6) * 25:.2f}")
print("Ou para maior eficiência")
gal18 = area//18
gal36 = ceil((area % 18) / 3.6)
print(f"{gal18:.0f} galões de 18 e {gal36:.0f} galões de 3.6 litros, que sairá por R${gal36 * 25 + gal18 * 80:.2f}")