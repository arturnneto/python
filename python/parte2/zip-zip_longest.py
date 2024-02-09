"""
zip - une iteráveis, une até a menor lista acabar
zip_longest - une ate a maior lista, preenche com valores padroes
caso a menor acabe
"""
from itertools import zip_longest, count

indice = count()
cidades = ['floripa', 'sao jose', 'biguacu', 'palhoca', 'braco do norte']
estados = ['sc', 'sc', 'sc', 'sc']

cidades_estados = zip(
    indice,
    cidades,
    estados,
)
for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)

print('#' * 18)

cidades2 = ['floripa', 'sao jose', 'biguacu', 'palhoca', 'braco do norte']
estados2 = ['sc', 'sc', 'sc', 'sc']

cidades_estados2 = zip_longest(cidades2, estados2, fillvalue='Estado')
print(list(cidades_estados2))
