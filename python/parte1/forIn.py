texto = "Python"
for letra in texto:
    print(letra)

for n in range(0, 8, 2):  # 0 -> começo | 8 -> fim | 2 -> de quantas em quantas
    print(n)

print("$$$$")

for n in range(0, 100, 1):
    if n % 8 == 0:
        print(n)

nova_string = ""
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)


