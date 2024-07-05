import random, time

print("Vamos jogar pedra, papel e tesoura. Melhor de três.")
time.sleep(1)

player = 0
com = 0
jogadas_possiveis = ["pedra", "papel", "tesoura"]

while com < 3 or player < 3:
    j1 = input("Pedra, papel e tesoura! ")
    cchoice = random.choice(jogadas_possiveis)
    if j1 == cchoice:
        print("Empate! Ninguém ganha pontos.")
        time.sleep(1)
    elif j1 == "pedra"  and cchoice == "tesoura":
        print(f"Jogador escolheu {j1} e a maquina escolheu {cchoice}. Você ganhou um ponto.")
        player += 1
    


    
