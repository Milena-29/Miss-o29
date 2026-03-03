quantidadeMaiores10 = 0

somaMaiores10 = 0

for i in range(5):
    
    numero = int(input("Digite um número: "))
    
    if numero > 10:
        
        quantidadeMaiores10 += 1
        
        somaMaiores10 += numero


print("\nQuantidade de números maiores que 10:", quantidadeMaiores10)
print("Soma dos números maiores que 10:", somaMaiores10)
