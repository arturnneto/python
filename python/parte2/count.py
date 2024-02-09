from itertools import count

contador = count(start=5, step=0.5)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break

lista = ['Artur', 'Jorge', 'Amorim', 'Neto']
lista = zip(contador, lista)
print(list(lista))
