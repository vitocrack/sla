i = [45,56,78,24,6,12395,2456,14679,235,14,3,2343,74,21,8555,4356,6743568,53]
con = 0

while (con < len(i)):
    print(i[con])
    if i[con] == 74:
        print("Achamo o 74.")
        break
    else:
        con += 1

print("Pronto.")