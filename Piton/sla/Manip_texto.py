import os
if not(os.path.isdir('/Users/VitorAraujo/Desktop/ProjetoAI')):
    os.mkdir("/Users/VitorAraujo/Desktop/ProjetoAI")

cpf = input("Qual seu cpf? ")
arq = "/Users/VitorAraujo/Desktop/ProjetoAI/" + cpf + ".txt"

print(arq)
algo = input("Escreva sua idade: ")
with open(arq, 'w') as arq:
    c = arq.write(algo)
# for i in range(1, 5):
#     file1.write(algo)
# c = file1.write()
# print(c)

     