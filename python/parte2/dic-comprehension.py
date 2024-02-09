lista = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

d1 = {x: y*2 for x, y in lista}
d2 = {x.upper(): y for x, y in lista}
d3 = {x: y for x, y in range(5)}
d4 = {f'Chave_{x}': x**2 for x in range(5)}
print(d1)
