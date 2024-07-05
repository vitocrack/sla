def maior(l):
    lista = []
    n1, n2 ,n3 = map(int, (l.split(' ')))
    lista.extend([n1, n2, n3])
    print(max(lista))

n = input("Digite três numeros (0 0 0):")
maior(n)