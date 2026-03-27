##  Elaborar um programa que leia uma senha e informe se ela é válida ou não. Para ser válida a senha
##  deve conter letras maiúsculas, minúsculas e números. Além disso, a senha deve possuir entre 8 e 12
##  caracteres.

print()
senha = input("Senha: ")

if len(senha) < 8 or len(senha) > 12:
    print("Senha invalida, a senha deve conter entre 8 e 12 caracteres.")
else: 
    maiuscula = 0
    minuscula = 0
    numero = 0
    
    for char in senha:
        if char.isupper():
            maiuscula += 1
        elif char.islower():
            minuscula += 1
        elif char.isdigit():
            numero += 1
        
        if maiuscula > 0 and minuscula > 0 and numero > 0:
            print("Senha válida.")
            break
    else:
        print("Senha inválida, a senha deve conter letras maiúsculas, minúsculas e números.")