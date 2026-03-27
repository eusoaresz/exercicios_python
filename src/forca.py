##   Elaborar um programa que exiba inicialmente o menu inicial apresentado a seguir:
##   1. Incluir Palavra
##   2. Listar Palavras
##   3. Alterar Dica
##   4. Excluir Palavra
##   5. Listar Palavras em Ordem
##   6. Finalizar
##   O programa deve ler palavra e dica, armazenando os dados em 2 listas distintas. Salvar os
##   dados ao final do programa em arquivo texto. No início, ler o arquivo e atribuir para as
##   listas. Estes dados serão utilizados em um jogo de descubra a palavra (Jogo da Forca).

import random

palavras = []
dica = []

while True:                                         ##Laço de repetição para exibir o menu e processar as opções do usuário
    print("+===========MENU:===========+")                                ##Exibe o menu de opções para o usuário
    print("|1. Incluir Palavra         |")
    print("|2. Listar Palavras         |")
    print("|3. Alterar Dica            |")
    print("|4. Excluir Palavra         |")
    print("|5. Listar Palavras em Ordem|")
    print("|6. Finalizar               |")
    print("+===========================+")
    opcao = input("Escolha uma opção:  ")
    print()

    if opcao == "1":                                 ##Opção para incluir uma nova palavra e sua dica
        nova_palavra = input("Digite a nova palavra: ")
        nova_dica = input("Digite a dica para a palavra: ")
        palavras.append(nova_palavra)
        dica.append(nova_dica)

    elif opcao == "2":                               ##Opção para listar as palavras e suas dicas
        if not palavras:
            print("Voçe não escolheu nenhuma palavra, adicione uma palavra.")
        else:
            for i in range(len(palavras)):                  ##Laço para percorrer as listas de palavras e dicas e exibir cada palavra com sua respectiva dica
                print(f"{palavras[i]} - Dica: {dica[i]}")

    elif opcao == "3":                                 ##Opção para alterar a dica de uma palavra existente
        palavra_alterar = input("Digite a palavra para alterar a dica: ")
        if palavra_alterar in palavras:                   ##Verifica se a palavra existe na lista de palavras, caso ela nao exista, "Palavra não encontrada"
            indice = palavras.index(palavra_alterar)     ##Obtém o índice da palavra na lista
            nova_dica = input("Digite a nova dica: ")    ##Solicita a nova dica para a palavra
            dica[indice] = nova_dica                      ##Atualiza a dica correspondente à palavra no índice encontrado
        else:
            print("Palavra não encontrada.")
    
    elif opcao == "4":
        palavra_excluir = input("Digite a palavra que deseja excluir: ")
        if palavra_excluir in palavras:                   ##Verifica se a palavra existe na lista de palavras, caso ela nao exista, "Palavra não encontrada"
            indice = palavras.index(palavra_excluir)     ##Obtém o índice da palavra na lista
            palavras.pop(indice)                         ##Remove a palavra da lista de palavras usando o índice encontrado
            dica.pop(indice)                             ##Remove a dica correspondente à palavra da lista de dicas usando o mesmo índice
        else:
            print("Palavra não encontrada.")
    
    elif opcao == "5":
        palavras_ordenadas = sorted(palavras)          ##Cria uma nova lista de palavras ordenada alfabeticamente usando a função sorted()
        for palavra in palavras_ordenadas:              ##Laço para percorrer a lista de palavras ordenada e exibir cada palavra
            print(palavra)
    
    elif opcao == "6":                                 ##Opção para finalizar o programa
        print("Voçê finalizou o programa.")
        break