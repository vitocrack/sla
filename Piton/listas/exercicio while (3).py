div = []
num = int(input("Digite um valor: "))

for i in range(1, num ):
    if num % i == 0:
        div.append(i)

for j in div:
    print(j, end='')
    if j == max(div):
        print(end=" = ")
    else:
        print(end=" + ")
print(sum(div))