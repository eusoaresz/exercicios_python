import random  # Importa o módulo 'random' para gerar números aleatórios (usado no sorteio dos símbolos)
import time    # Importa o módulo 'time' para usar pausas (time.sleep) na animação do giro
import os      # Importa o módulo 'os' para executar comandos do sistema operacional (limpar tela)

# ── Cores ANSI ─────────────────────────────────────────────────
# Códigos de escape ANSI que o terminal interpreta como cores e estilos de texto.
# Cada variável guarda uma string especial que, ao ser impressa, muda a cor/estilo do texto.
RST = "\033[0m"   # Reset: cancela qualquer cor ou estilo ativo, voltando ao padrão do terminal
BD  = "\033[1m"   # Bold (negrito): deixa o texto mais grosso/brilhante
DIM = "\033[2m"   # Dim (esmaecido): deixa o texto mais apagado/fraco
RED = "\033[91m"  # Vermelho brilhante: usado para erros e mensagens de perda
GRN = "\033[92m"  # Verde brilhante: usado para saldo, vitória e valores positivos
YLW = "\033[93m"  # Amarelo brilhante: usado para prompts de entrada do usuário
BLU = "\033[94m"  # Azul brilhante: disponível para uso futuro
MGT = "\033[95m"  # Magenta (rosa) brilhante: usado na mensagem de despedida
CYN = "\033[96m"  # Ciano brilhante: usado nas bordas decorativas do jogo
WHT = "\033[97m"  # Branco brilhante: usado para destacar o nome do jogador


def limpar():
    # Limpa o terminal antes de exibir o jogo
    # 'os.name == "nt"' verifica se o sistema é Windows (NT = New Technology, nome interno do Windows)
    # No Windows usa o comando 'cls'; em Linux/Mac usa 'clear'
    os.system("cls" if os.name == "nt" else "clear")


def ler_valor_positivo(msg):
    # Função que fica em loop até o usuário digitar um número válido e maior que zero
    while True:
        # Exibe a mensagem em amarelo, lê a entrada e troca vírgula por ponto
        # (para aceitar tanto "10,50" quanto "10.50" como entrada válida)
        entrada = input(f"{YLW}{msg}{RST}").replace(",", ".")
        try:
            valor = float(entrada)   # Tenta converter a entrada para número decimal (float)
            if valor <= 0:
                # Se o número for zero ou negativo, avisa e repete o loop
                print(f"  {RED}✘ Digite um valor maior que zero.{RST}")
            else:
                return valor  # Retorna o valor válido para quem chamou a função
        except ValueError:
            # Se a conversão falhar (ex: usuário digitou "abc"), cai aqui e avisa
            print(f"  {RED}✘ Valor inválido. Digite somente números.{RST}")


def cabecalho():
    # Exibe o título do jogo dentro de uma caixa decorativa com bordas em ciano
    print(f"{CYN}╔══════════════════════════════════════════╗{RST}")  # Linha superior da caixa
    print(f"{CYN}║{RST}  {YLW}{BD}  🎰   C A Ç A - N Í Q U E L   🎰  {RST}  {CYN}║{RST}")  # Título em amarelo e negrito
    print(f"{CYN}║{RST}  {DIM}Alinhe 3 símbolos iguais e ganhe {GRN}5×{RST}{DIM} a aposta!{RST} {CYN}║{RST}")  # Regra do jogo esmaecida
    print(f"{CYN}╚══════════════════════════════════════════╝{RST}")  # Linha inferior da caixa


def painel_saldo(nome, saldo):
    # Exibe um painel com o nome do jogador e o saldo atual formatados dentro de uma caixa
    barra = f"{GRN}R$ {saldo:.2f}{RST}"  # Formata o saldo em verde com 2 casas decimais (ex: R$ 100.00)
    print(f"\n{CYN}  ┌──────────────────────────────────────┐{RST}")  # Borda superior simples
    print(f"{CYN}  │{RST}  {BD}👤 Jogador:{RST} {WHT}{nome}{RST}")    # Nome do jogador em branco brilhante
    print(f"{CYN}  │{RST}  {BD}💰 Saldo:  {RST} {barra}")              # Saldo atual em verde
    print(f"{CYN}  └──────────────────────────────────────┘{RST}")  # Borda inferior simples


def girar_caca_niquel(figuras):
    simbolos = list(figuras)  # Transforma a string de emojis em lista: ['🍉', '🍇', '🍊']

    print(f"\n{CYN}  ╔═══════╦═══════╦═══════╗{RST}")  # Borda superior da máquina caça-níquel com 3 colunas

    # ── Animação de giro ──────────────────────────────────────────
    for i in range(18):  # Repete 18 frames de animação (o giro visível antes de parar)
        # Sorteia aleatoriamente 3 símbolos para exibir neste frame da animação
        r = [simbolos[random.randint(0, 2)] for _ in range(3)]

        # Monta a linha do frame com bordas e os 3 símbolos sorteados
        linha = (
            f"\r{CYN}  ║{RST}  {r[0]}   "   # '\r' volta o cursor ao início da linha (sobrescreve o frame anterior)
            f"{CYN}║{RST}  {r[1]}   "
            f"{CYN}║{RST}  {r[2]}   "
            f"{CYN}║{RST}"
        )
        print(linha, end="", flush=True)  # Imprime sem quebrar linha; flush=True força a exibição imediata

        # Nos primeiros 10 frames gira rápido (0.10s); depois desacelera (0.18s) para simular parada
        time.sleep(0.10 if i < 10 else 0.18)

    # ── Resultado final ───────────────────────────────────────────
    # Sorteia os 3 símbolos definitivos que valerão como resultado da rodada
    resultado = [simbolos[random.randint(0, 2)] for _ in range(3)]

    # Monta e exibe a linha final com os símbolos do resultado, sobrescrevendo o último frame
    linha_final = (
        f"\r{CYN}  ║{RST}  {resultado[0]}   "
        f"{CYN}║{RST}  {resultado[1]}   "
        f"{CYN}║{RST}  {resultado[2]}   "
        f"{CYN}║{RST}"
    )
    print(linha_final)                               # Imprime o resultado final com quebra de linha
    print(f"{CYN}  ╚═══════╩═══════╩═══════╝{RST}") # Borda inferior da máquina caça-níquel

    return "".join(resultado)  # Junta os 3 emojis em uma única string e retorna (ex: '🍉🍉🍉')


def separador():
    # Imprime uma linha horizontal decorativa para separar visualmente as rodadas
    print(f"  {CYN}{'─' * 40}{RST}")  # Gera 40 traços '─' em ciano


# ── INÍCIO DO JOGO ─────────────────────────────────────────────
limpar()    # Limpa o terminal para o jogo começar com a tela limpa
cabecalho() # Exibe o título/cabeçalho do jogo

print()  # Linha em branco para espaçamento visual
nome  = input(f"  {YLW}👤 Nome do apostador: {RST}")           # Lê e armazena o nome do jogador
saldo = ler_valor_positivo("  💰 Valor do depósito: R$ ")      # Lê o depósito inicial validado

figuras = "🍉🍇🍊"  # String com os 3 emojis que representam os símbolos do caça-níquel

# Exibe os símbolos disponíveis logo após o depósito
print(f"\n  {CYN}Símbolos disponíveis: {figuras[0]}  {figuras[1]}  {figuras[2]}{RST}")

# ── Loop principal do jogo ────────────────────────────────────
# O jogo continua enquanto o jogador tiver saldo maior que zero
while saldo > 0:
    painel_saldo(nome, saldo)  # Exibe o painel com nome e saldo atualizado a cada rodada

    # Pergunta se o jogador quer apostar; .strip() remove espaços, .lower() converte para minúscula
    jogar = input(f"\n  {YLW}Deseja apostar? (s/n): {RST}").strip().lower()

    if jogar != "s":
        # Se a resposta não for 's', encerra o jogo voluntariamente
        print(f"\n  {MGT}Até a próxima, {BD}{nome}{RST}{MGT}! Boa sorte! 🍀{RST}")
        break  # Sai do while, encerrando o loop principal

    aposta = ler_valor_positivo("  💵 Valor da aposta: R$ ")  # Lê o valor da aposta com validação

    if aposta > saldo:
        # Se a aposta for maior que o saldo disponível, avisa e volta ao início do loop (não debita)
        print(f"\n  {RED}✘ Aposta maior que o saldo disponível!{RST}")
        continue  # Volta ao início do 'while' sem executar o restante da rodada

    saldo -= aposta  # Desconta o valor apostado do saldo antes de girar (o jogo toma a aposta)

    jogo = girar_caca_niquel(figuras)  # Executa a animação e retorna a string com os 3 símbolos sorteados

    conjunto = set(jogo)  # Converte a string resultado em um conjunto (set), que remove duplicatas
                           # Ex: '🍉🍉🍉' → {'🍉'} (1 elemento) | '🍉🍇🍉' → {'🍉','🍇'} (2 elementos)

    print()  # Linha em branco antes da mensagem de resultado

    if len(conjunto) == 1:
        # Se o set tem 1 elemento → todos os 3 símbolos são iguais → JACKPOT!
        premio = aposta * 5           # O prêmio é 5 vezes o valor apostado
        saldo += premio               # Adiciona o prêmio ao saldo do jogador
        print(f"  {GRN}{BD}🎉 JACKPOT! Parabéns, {nome}! Você ganhou R$ {premio:.2f}! 💵💸{RST}")
    elif len(conjunto) == 2:
        # Se o set tem 2 elementos → 2 símbolos iguais e 1 diferente → quase ganhou, sem prêmio
        print(f"  {YLW}😅 Quase lá! Foi por pouco... Tente novamente!{RST}")
    else:
        # Se o set tem 3 elementos → todos os 3 símbolos são diferentes → perdeu
        print(f"  {RED}😞 Todas diferentes. Mais sorte na próxima rodada!{RST}")

    print(f"\n  Saldo após a rodada: {GRN}{BD}R$ {saldo:.2f}{RST}")  # Exibe o saldo atualizado após a rodada
    separador()  # Imprime a linha separadora visual entre as rodadas

# ── Pós-jogo ──────────────────────────────────────────────────
if saldo <= 0:
    # Se o saldo zerou (saiu do while por saldo insuficiente), exibe mensagem de fim por falta de fundos
    print(f"\n  {RED}{BD}💸 Saldo esgotado! Jogo encerrado.{RST}")

print()  # Linha em branco antes da tela final
# Exibe a tela de encerramento com o saldo final dentro de uma caixa decorativa
print(f"{CYN}╔══════════════════════════════════════════╗{RST}")  # Borda superior
print(f"{CYN}║{RST}  {BD}Obrigado por jogar, {nome}!{RST}")        # Agradecimento com nome do jogador
print(f"{CYN}║{RST}  Saldo final: {GRN}{BD}R$ {saldo:.2f}{RST}")   # Saldo final formatado em verde
print(f"{CYN}╚══════════════════════════════════════════╝{RST}")  # Borda inferior
print()  # Linha em branco final para o cursor não ficar colado na última linha