numero = int(input("Digite um número: "))

soma = 0

while numero != 0:
    
    soma += numero
    
    print("\nSoma: ", soma)
    
    numero = int(input("Digite um número: "))

print("Programa encerrado!")
print("Soma final:", soma)