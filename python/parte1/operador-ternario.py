logged_user = False

if logged_user:
    msg = "Você está logado."
else:
    msg = "Você precisa fazer login."

print(msg)

print()  ########################## como poderia ser feito com operador ternario:

msg = "Você está logado." if logged_user else "Você precisa fazer login."
print(msg)
