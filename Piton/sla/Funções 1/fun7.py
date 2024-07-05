def pagamento(hrs, salario):
    if hrs > 40:
        hrs -= 40
        x = salario + hrs * (salario * 0.50)
    print(x)

pagamento(48, 1300)  
