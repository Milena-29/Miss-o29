senha = input("Digite a senha: ")

tem_maiuscula = False

tem_minuscula = False

tem_numero = False

tem_especial = False

for i in senha:  
    if i.isupper():
        tem_maiuscula = True
    elif i.islower():
        tem_minuscula = True
    elif i.isdigit():
        tem_numero = True
    elif i in string.punctuation:
        tem_especial = True

if len(senha) < 8:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres!")

if tem_maiuscula == False:
    print("Senha inválida. A senha deve ter pelo menos uma letra maiúscula!")

elif tem_minuscula == False:
    print("Senha inválida. A senha deve ter pelo menos uma letra minúscula!")

elif tem_numero == False:
    print("Senha inválida. A senha deve ter pelo menos um número!")

elif tem_especial == False:
    print("Senha inválida. A senha deve ter pelo menos um caractere especial!")

else:
    print("Senha válida e forte!")