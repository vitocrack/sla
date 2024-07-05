num = int(input("Digite um valor: "))
sla = 0

while num != 0:
    digito = num % 10
    sla += digito
    num //= 10

print(sla)