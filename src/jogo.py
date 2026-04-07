import random
import time
from pathlib import Path
from colorama import init, Fore

# inicializa o colorama
init(autoreset=True)

print(Fore.BLUE + "===== JOGO DE DESCUBRA A PALAVRA =====")
nome = input(Fore.MAGENTA + "Nome do Jogador: ")

hora_inicial = time.time()

palavras = []
dicas = []
erros = 0
max_erros = 6

def carrgar_palavras():
    try:
        arquivo = Path(__file__).with_name("palavras.txt")
        with arquivo.open("r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha or ";" not in linha:
                    continue
                partes = linha.split(";")
                palavras.append(partes[0].strip())
                dicas.append(partes[1].strip())
    except FileNotFoundError as e:
        print(Fore.RED + f"Erro... Arquivo com as Palavras não existe: {arquivo}")
        exit(1)

carrgar_palavras()
print(palavras)
print(dicas)

num = random.randint(0, len(palavras)-1)

palavra = palavras[num].upper()
dica = dicas[num]

letras_usadas = [palavra[0]]
palavra_escondida = ["_"] * len(palavra)

for i in range(0, len(palavra)):
    if palavra[i] == palavra[0]:
        palavra_escondida[i] = palavra[0]

#print(palavra)
#print(palavra_escondida)

carinhas = [
    "😀😀😀😀😀",
    "😡😀😀😀😀",
    "😡😡😀😀😀",
    "😡😡😡😀😀",
    "😡😡😡😡😀",
    "😡😡😡😡😡"
]

def mostra_status():
    print(Fore.YELLOW + f"Status: {carinhas[erros]}")
    print(Fore.GREEN + f"Palavra: {' '.join(palavra_escondida)}")
    print(Fore.CYAN + f"Erros: {erros}/{max_erros}")

########################### Programa Principal
while True:

    #verifica se perdeu
    if erros == max_erros:
        print(Fore.RED + f"Perdeu... A palavra era {palavra} 😣")
        break

    mostra_status()

    #verifica se ganhou
    if "".join(palavra_escondida) == palavra:
        print(Fore.BLUE + f"Párabens {nome}! Acertou!")
        break

    letra = input("\nLetra ou * para ver dica (vale 1 vida): ").strip().upper()

    if letra == "*":
        if "*" in letras_usadas:
            print(Fore.RED + "Dica já foi informada")
        else:
            print(Fore.YELLOW + f"Dica: {dica}")
            letras_usadas.append("*")
            erros += 1
        continue

    if letra == "" or len(letra) > 1:
        print(Fore.RED + "Digite apenas uma letra")
        continue

    if letra in letras_usadas:
        print(Fore.RED + f"Voçê já informou a letra: '{letra}")
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        print(Fore.GREEN + f"Letra '{letra}' encontrada!")
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra
    else:
        erros += 1
        print(Fore.RED + f"Letra: '{letra}' NÃO EXISTE na palavra")

hora_final = time.time()
duracao = hora_final - hora_inicial
print(f"Jogo durou: {duracao:.2f} segundos")