num = []
while True:
    n = int(input("Digite número: "))
    if n < 0:
        break
    num.append(n)

print(f"O maior número inserido foi {max(num)}. O menor foi {min(num)}.")
