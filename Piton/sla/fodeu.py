# 1
# k = int(input())

# con = 1
# soma = []
# while con <= k:
#     cal = 5 * (con - 1) - con ** 2
#     soma.append(cal)
#     con += 1

# fim = sum(soma)
# sla = ''
# for i in soma:
#     sla += str(i) + ' '
# print(f"Sequência:\n{sla}\n\nPara k = {k}, o valor do somatório é: {fim}")

#2

sla = input()
l = sla.split()
l = list(map(int, l))
rem = int(input())
if rem in l:
    l.pop(l.index(rem))
    print(sorted(l))
else:
    print("O elemento não existe na lista")

