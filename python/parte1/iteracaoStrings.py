frase = input('Digite uma frase para capitalizar: ')
contador = 0
nova_string = ""

while contador < len(frase):
    letra = frase[contador]
    if letra == " ":
        nova_string += " "
        nova_string += frase[(contador + 1)].upper()
        contador += 1
    else:
        nova_string += letra
    contador += 1

print(nova_string[0].upper()+nova_string[1:])
