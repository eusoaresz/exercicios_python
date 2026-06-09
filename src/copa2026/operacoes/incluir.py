import requests
from rich import print
from config import API_URL

def incluir():
    print("\n[bold green]Inclusão de Seleção[/bold green]")

    nome = input("Nome...............: ")
    continente = input("Continente.........: ")
    numCopas = int(input("Nº de Copas........: "))
    destaques = input("Jogadores Destaques: ")
    chanceTitulo = float(input("Chance de Título...: "))

    dados = {
        "nome": nome,
        "continente": continente,
        "numCopas": numCopas,
        "destaques": destaques,
        "chanceTitulo": chanceTitulo
    }

    resposta = requests.post(API_URL, json=dados)

    if resposta.status_code in [200, 201]:
        print("[green]Seleção cadastrada com sucesso![/green]")
    else:
        print(f"[red]Erro: {resposta.status_code}[/red]")