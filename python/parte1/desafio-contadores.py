contador = 0
outro_contador = 10

while contador < 8 and outro_contador > 2:
    contador += 1
    outro_contador -= 1
    print(contador, outro_contador)

for p, r in enumerate(range(0, 200, 11)):
    print(p, r)