import random
import time


def ler_valor_positivo(mensagem):
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def girar_caca_niquel(figuras):
    jogo = ""
    print("Resultado: ", end="")
    for _ in range(3):
        num = random.randint(0, 2)
        simbolo = figuras[num]
        print(simbolo, end="", flush=True)
        time.sleep(1)
        jogo += simbolo
    print()
    return jogo


nome = input("Nome do apostador: ")
saldo = ler_valor_positivo("Quanto você quer depositar? R$ ")

figuras = "🍉🍇🍊"

print("\nBem-vindo(a),", nome)
print(f"Saldo inicial: R$ {saldo:.2f}")
print(f"Símbolos do jogo: {figuras[0]} {figuras[1]} {figuras[2]}")

while saldo > 0:
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
    jogar = input("Deseja fazer uma aposta? (s/n): ").strip().lower()

    if jogar != "s":
        print("Você escolheu encerrar. Até a próxima!")
        break

    aposta = ler_valor_positivo("Digite o valor da aposta: R$ ")

    if aposta > saldo:
        print("O valor da aposta ultrapassou o valor da sua carteira.")
        continue

    saldo -= aposta
    jogo = girar_caca_niquel(figuras)
    conjunto = set(jogo)

    if len(conjunto) == 1:
        premio = aposta * 5
        saldo += premio
        print(f"Parabéns {nome}, você ganhou R$ {premio:.2f} 💵💸")
    elif len(conjunto) == 2:
        print("Que azar... foi por pouco... continue jogando!")
    else:
        print("Todas diferentes... mas não desista!")

    print(f"Saldo após a rodada: R$ {saldo:.2f}")

if saldo <= 0:
    print("\nSeu saldo acabou. Jogo encerrado.")

print(f"Saldo final: R$ {saldo:.2f}")