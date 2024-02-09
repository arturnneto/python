#  Função que retorna uma saudação
def saudar(saudacao, nome):
    return f'{saudacao}, meu nome é {nome}'


var = saudar('Olá', 'Artur')
print(var)


# Função que retorna a soma de três números
def somar(x, y, z):
    return x + y + z


var2 = somar(2, 5, 7)
print(var2)


# Função que soma X com ele mesmo multiplicado pelo percentual do número Y
def somar_percentual(x, y):
    y /= 100
    return x + x*y


var3 = somar_percentual(100, 5)
print(var3)


# Função FizzBuzz
def fizz_buzz(x):
    if x % 5 == 0 and x % 3 == 0:
        return 'FizzBuzz'
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'Buzz'
    return x


var4 = fizz_buzz(25)
print(var4)
