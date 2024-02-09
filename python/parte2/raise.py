"""
Captura o erro e relança o mesmo novamente em outro try except
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)


# criando erros personalizados
def dividir(n1, n2):
    if n2 == 0:
        raise ValueError
    return n1 / n2
