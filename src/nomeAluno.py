##  Elaborar um programa que leia o nome completo de um aluno. Valide o nome para que seja composto.
##  Exiba apenas o primeiro nome do aluno em letras maiúsculas.

nome_completo = input("Nome Completo: ")

if nome_completo.strip() and len(nome_completo.split()) >= 2:
    primeiro_nome = nome_completo.split()[0]

    print(f"Nome no Crachá: {primeiro_nome.upper()}")
else:
    print("Nome inválido, o nome deve ser composto por pelo menos duas palavras.")