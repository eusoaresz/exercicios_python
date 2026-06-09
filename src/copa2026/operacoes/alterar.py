import requests

from rich import print

from config import API_URL

def alterar():
    id = input("ID da seleção: ")

    consulta = requests.get(f"{API_URL}/{id}")

    if consulta.status_code != 200:
        print("[red]Seleção não encontrada[/red]")
        return

    selecao = consulta.json()

    print("\n[bold yellow]Alteração[/bold yellow]")

    nome = input(f"Nome [{selecao['nome']}]: ") \
        or selecao["nome"]

    continente = input(
        f"Continente [{selecao['continente']}]: "
    ) or selecao["continente"]

    numCopas = input(
        f"Copas [{selecao['numCopas']}]: "
    )

    destaques = input(
        f"Destaques [{selecao['destaques']}]: "
    ) or selecao["destaques"]

    chance = input(
        f"Chance [{selecao['chanceTitulo']}]: "
    )

    dados = {
        "nome": nome,
        "continente": continente,
        "numCopas": int(numCopas) if numCopas else selecao["numCopas"],
        "destaques": destaques,
        "chanceTitulo": float(chance) if chance else selecao["chanceTitulo"]
    }

    resposta = requests.put(
        f"{API_URL}/{id}",
        json=dados
    )

    if resposta.status_code == 200:
        print("[green]Registro alterado![/green]")
    else:
        print("[red]Erro na alteração[/red]")