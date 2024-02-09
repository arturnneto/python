from dados import lista, produtos, pessoas
from functools import reduce

"""
Aplica uma função no iterável e reduz a apenas um valor
"""

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))  # media de preços dos produtos

media_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(media_idades / len(pessoas))
