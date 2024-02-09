cpf = input("Digite o CPF a ser analisado: ")

# Checa se o CPF digitado contém apenas números.
if not cpf.isnumeric():
    print('Por favor, digite apenas números.')
    exit()

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

# Cria o resultado final do CPF.
novo_cpf = cpf[:9] + str(digito_1) + str(digito_dois)

# Checa se o CPF é uma sequencia
sequencia = novo_cpf == novo_cpf[0] * len(novo_cpf)

# Retorna se o CPF digitado é valido ou não.
if cpf == novo_cpf and not sequencia:
    print('CPF Válido.')
else:
    print('CPF Inválido')
