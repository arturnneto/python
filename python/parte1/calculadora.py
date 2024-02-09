try:
    primeiro_numero = input('Digite um numero: ')
    segundo_numero = input('Digite outro número: ')
    operacao = input('Digite o sinal da operação desejada: ')

    primeiro_numero = int(primeiro_numero)
    segundo_numero = int(segundo_numero)

    if operacao == "+":
        print(primeiro_numero + segundo_numero)
    elif operacao == "-":
        print(primeiro_numero - segundo_numero)
    elif operacao == "*":
        print(primeiro_numero * segundo_numero)
    elif operacao == "/":
        print(primeiro_numero / segundo_numero)

except:
    print("Não foi possível realizar a operação.")
