variavel = 'valor'


def func():
    variavel = 'outro valor'
    print(variavel)


def func2():
    print(variavel)


func()
func2()
print(variavel)