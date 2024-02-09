from dados import produtos, pessoas, lista

"""
Recebe uma função e filtra os resultados com base nos argumentos.
Pode usar uma função def caso a função lambda seja muito complexa.
"""

nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5] --> list comprehension
print(list(nova_lista))

print()

lista_nova = filter(lambda p: p['preco'] > 10, produtos)

for produto in lista_nova:
    print(produto)

print()


def filtra(produto2):
    if produto2['preco'] > 50:
        return True


outra_lista = filter(filtra, produtos)

for produto in outra_lista:
    print(produto)

print()


def filtra_idade(pessoa2):
    if pessoa2['idade'] > 21:
        return True


ultima_lista = filter(filtra_idade, pessoas)

for pessoa in ultima_lista:
    print(pessoa)