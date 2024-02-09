from random import randint
numero = str(randint(100000000, 999999999))
cpf = numero

# Variáveis para a primeira conta
contador = 10
armazenar_conta = 0

# Itera os números do CPF, realizando as contas necessárias.
for v, valor1 in enumerate(cpf[:9]):
    conta = int(valor1) * contador
    armazenar_conta += conta
    contador -= 1

# Faz a conta para descobrir o primeiro dígito.
descobrir_digito_1 = 11 - (armazenar_conta % 11)
if descobrir_digito_1 > 9:
    digito_1 = 0
else:
    digito_1 = descobrir_digito_1

# Variáveis para a segunda conta.
contador_dois = 11
armazenar_conta_dois = 0

# Realiza as primeiras contas do segundo dígito.
for v, valor2 in enumerate(cpf[:9]):
    conta_dois = int(valor2) * contador_dois
    armazenar_conta_dois += conta_dois
    contador_dois -= 1

# Conta final para descobrir o número dois.
digito_dois = 11 - ((armazenar_conta_dois + (digito_1 * 2)) % 11)
if len(str(digito_dois)) > 1:
    digito_dois = 0

# Cria o resultado final do CPF.
novo_cpf = cpf[:9] + str(digito_1) + str(digito_dois)
var = len(novo_cpf)

print(novo_cpf)
