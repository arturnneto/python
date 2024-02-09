lista = [1, {2, 5}, 'teste', True, 'ablabla', (1, 2, 3), {50: 50}, 5.2, False]

for item in lista:
    if isinstance(item, bool):
        print(item)
    if isinstance(item, int or float):
        print(item)
