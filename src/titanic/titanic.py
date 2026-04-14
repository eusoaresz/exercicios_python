import csv

#lista (vetor) de dicionarios (objetos) com os passageiros do Titanic
titanic = []

#le os dados do arquivo e atribui para a lista (titanic)
with open("titanic/train.csv") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        titanic.append(linha)

# print(titanic[0])
# print(titanic[0]['Name'])

def titulo(texto, traco="-"):
    print()
    print(texto.upper())
    print(traco*40)

def compara_sexo():
    titulo("Compara Passageiros por Sexo x Sobreviventes")
    # Masculino: xxx
    # - Sobreviventes: xxx
    # - Mortos: xxx

    with open("titanic/train.csv") as arq:
        dados = csv.DictReader(arq)
        masculino = 0
        feminino = 0
        survived = 0
        for linha in dados:
            if linha['Sex'] == 'male':
                masculino += 1
            else:
                feminino += 1
            if masculino == 0 and linha['Survived'] == '1':
                survived += 1

    print(f"Masculino: {masculino}")
    print(f"Feminino: {feminino}")
    print(f"Sobreviventes: {survived}")

def media_idosos():
    titulo("Média de Idade e Top 10 Idosos")
    # Media de de idade dos passageiros: xxx
    # Top 10+ idosos:
    # 1. Nome - Idade
    # 2. Nome - Idade
    # ...

def compara_classe():
    titulo("Comparação dos Passageiros Classe x Sobreviventes")
    # 1° Classe: xxx
    # - Sobreviventes: xxx
    # - Mortos: xxx

    # 2° Classe: xxx
    # - Sobreviventes: xxx
    # - Mortos: xxx

    # 3° Classe: xxx
    # - Sobreviventes: xxx
    # - Mortos: xxx

while True:
    titulo("Passageiros do Titanic", "=")
    print("1. comparação por Sexo e Sobreviventes")
    print("2. Média de Idade e Top 10 +Idosos")
    print("3. Comparção por Classe e Sobreviventes")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        compara_sexo()
    else:
        break