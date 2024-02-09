"""
Serve para criar uma função que recebe argumentos que serão usados posteriormente
Neste caso, não precisa ficar enviando parâmetros de -bom dia- ou -boa noite-
sempre que for chamar a função de novo
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Artur'))
print(falar_boa_noite('Artur'))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
print(duplicar(5))
