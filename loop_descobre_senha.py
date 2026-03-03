senha_correta = "SenhaSecreta"

tentativa = input("Digite a senha: ")

while tentativa != senha_correta:
    
    print("\nSenha incorreta! Tente novamente.")
    
    tentativa = input("Digite a senha: ")

print("Acesso permitido.")