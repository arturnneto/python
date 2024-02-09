import sys
import time
"""
Função que sabe pausar em determinado momento
"""

lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)

print(next(lista))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


# gerador:
l2 = (x for x in range(10000))  # generator
l3 = [x for x in range(10000)]
print(sys.getsizeof(l2))
print(sys.getsizeof(l3))

"""
Ele nao salva todos os valores na memoria como a lista, ele salva conforme
for pedindo.

Porem a lista pode ser acessada por indice, o generator nao.

Yield salva o valor da função e pausa a mesma.
"""
print()


def generator(n=0):
    yield 1
    print('Continuando')
    yield 2
    print('Continuando...')
    yield 3
    print('Acabando')
    return 'Acabou!'


gen = generator(n=0)
for n in gen:
    print(n)
