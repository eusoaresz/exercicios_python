##  Elaborar um programa que leia uma palavra. Exiba a letra inicial (e suas ocorrências) e "_" nas demais
##  posições, conforme o exemplo.

palavra = input("Digite uma palavra: ")

# pega a primeira letra
inicial = palavra[0]

resultado = ""

for letra in palavra:
    if letra == inicial:
        resultado += letra + " "
    else:
        resultado += "_ "

print(resultado.strip())