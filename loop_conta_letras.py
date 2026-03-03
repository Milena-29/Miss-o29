texto = input("Digite um texto: ")

maiusculas = 0
minusculas = 0

for caractere in texto:
    if caractere.isupper():  
        maiusculas += 1
    elif caractere.islower(): 
        minusculas += 1

print("Número de letras maiúsculas: ", maiusculas)
print("Número de letras minúsculas: ", minusculas)