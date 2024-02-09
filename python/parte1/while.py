# while x < 6:
#     print(x)
#     x = x + 1
# print('fim.')

x = 0
while x < 6:
    if x == 3:
        x += 1  # x = x + 1
        continue  # continue pula os laços de baixo e pula para o próximo loop

    print(x)
    x += 1
print('fim.')

print()  ###################

y = 0
while y < 6:
    if y == 3:
        y += 1
        break  # quando a condiçao for verdadeira, o loop é parado

    print(y)
    y += 1
print('fim.')

print()  ###########################

a = 0
while a < 4:  # nesse loop, o loop externo vai executar cada vez que o loop interno chegar ao fim
    b = 0  # 2- a qual reinicia o loop interno, zerando o valor de b
    while b < 3:
        print(f'A vale {a} e B vale {b}')
        b += 1  # 1- aqui, quando b < 3, ele executa a linha de baixo
    a += 1
