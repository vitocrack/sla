l = [10,20,30,40,50,60,70,80,90,100]
while True:
    user = int(input("Insira um numero: "))
    if user in l:
        print(f"{user} está na lista, no indice {l.index(user)}.")
    elif user < 0:
        break
    else:
        print(f"{user} não está na lista.")
