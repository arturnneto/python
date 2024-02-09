d1 = {
    1: 'a',
    2: 'b',
    3: 'c'
}
v = d1
v[1] = 'd'  # neste caso, a mudança vai ocorrer na variavel E TAMBEM no dicionario
print(v)
print(d1)

v2 = d1.copy()  # agora a variavel pode ser alterada apenas em alguns casos, pois listas e outros dicionarios dentro
                # dele ainda serão alterados
print()

d1.pop(3)  # elimina um item do dicionario
d2 = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}
d1.update(d2)  # junção de dicionarios
