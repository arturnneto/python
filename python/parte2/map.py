from dados import produtos, pessoas, lista

"""
Executa uma função em todos os itens de um iterável.
Pode usar uma função def caso a função lambda seja muito complexa.
"""

nova_lista = map(lambda x: x * 2, lista)
# nova_lista = [x * 2 for x in lista]
print(list(nova_lista))

print()


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


precos = map(aumenta_preco, produtos)
for preco in precos:
    print(preco)

print()


def aumenta_idade(p):
    p['nova_idade'] = p['idade'] * 1.20
    return p


nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)