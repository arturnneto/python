contador = 1
acumulador = 1

while contador < 7:
    print(contador, acumulador)
    if contador > 5:
        break                                                           # <-----    \/

    acumulador += contador
    contador += 1
else:  # o else fecha o codigo quando ele chega ao fim, caso não fosse utilizado, o break printaria o fim, sendo que
    print("O loop chegou ao fim.")                                                        # o loop nao chegou ao fim.
