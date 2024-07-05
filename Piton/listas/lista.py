num1 = [6,5,4,3,2,1]
print(num1)

num2 = [7.5,8.6,9.7,10.8,11.9,12.1]
numeros = num1 + num2

print(numeros)

num1.pop(2)
print(numeros)

numeros.insert(1,20,)
numeros.insert(2,21)
print(numeros)

numeros.sort()
print(numeros)

print(f"Maior: {max(numeros)}\nMenor: {min(numeros)}")

print(sum(numeros))

print(int(sum(numeros) // len(numeros)))

