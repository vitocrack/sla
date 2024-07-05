estoque = ["mouse", "teclado", "placa de vídeo", "fone de ouvido"]
n_adicionado = 0 #contador de nome de produtos adicionados
n_removido = 0 #contador da quantidade de cada produto
qnt = [20, 14, 10, 32]
desc = ["com fio, preto/branco com led azul", "com fio, preto com leds de cor variável", "nvidia, modelo GeForce RTX" ,"bluetooth sem microfone, preto"]
print("Bem vindo ao SGE\n Insira qual atividade deseja prosseguir:")

while True:
    main = int(input("\n<0> Fechar programa\n<1> Visualizar situação atual de estoque\n<2> Adicionar/Remover produto\n<3> Acessar registro de tráfego"))
    if main == 0:
            print("Fechando programa...")
            break
        
    elif main == 1: #visualizar estoque     
        print(f"Lista de produtos:\n")
        for esto, quan, descr in zip(estoque, qnt, desc): #zip para o for funcionar em multiplas variáveis 
             print(f"Item: {esto}, Qnt: {quan}, Desc: {descr}")


    elif main == 2: #adicionar/remover estoque
        print(estoque)
        menu2 = int(input("Deseja:\n<1> Adicionar item\n<2> Remover item"))
        if menu2 == 1: #add item
            additem, addqnt = input.lower("Digite qual produto deseja adicionar e sua quantidade (ex: monitor 4): ".split())
            addqnt = int(addqnt)
            if not (additem in estoque): #caso seja um produto novo no estoque, o sistema solicitará uma descrição
                 addesc = input("Insira uma descrição ao produto: ")
                 desc.append(addesc)
            estoque.append(additem) #adiciona input do usuario para lista de nome de produtos
            qnt.append(addqnt) #adiciona input para lista de quantidades
            print("Item adicionado!")
            n_adicionado += 1 # contador de itens adicionados até agora

        else: #remover item
            delitem = input.lower("\nDigite qual produto deseja remover: ")
            if delitem in estoque: 
                qnt_remove = int(input("\nInsira quantidade que deseja retirar: "))
                index = estoque.index(delitem) #variavel que vai procurar o input do usuario na lista 'estoque', para depois devolver em qual posição o item da lista se localiza
                qnt[index] -= qnt_remove #vai subtrair a quantidade atual de um produto com a quantidade inserida pelo usuario
                if qnt[index] <= 0: 
                    print("\nQuantidade removida. Produto esgotou ")
                print("\nItem removido!")
                n_removido += 1 #contador de items removidos até agora
            else:
                 print("Erro, produto não encontrado!")
 
    elif main == 3: #registro
            print(f"{n_adicionado} produtos foram adicionados no momento.\n{n_removido} foram removidos no momento.")
       
    else:
         print("Valor inválido. Por favor tente novamente.")