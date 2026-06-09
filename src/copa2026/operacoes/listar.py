import requests

from rich.table import Table
from rich.console import Console

from config import API_URL

def listar():
    resposta = requests.get(API_URL)

    if resposta.status_code != 200:
        print("Erro ao consultar API")
        return

    dados = resposta.json()

    tabela = Table(title="Seleções Cadastradas")

    tabela.add_column("ID")
    tabela.add_column("Nome")
    tabela.add_column("Continente")
    tabela.add_column("Copas")
    tabela.add_column("Chance")
    tabela.add_column("Jogadores em Destaque")

    for item in dados:
        tabela.add_row(
            str(item["id"]),
            item["nome"],
            item["continente"],
            str(item["numCopas"]),
            f'{item["chanceTitulo"]}%',
            item["jogadoresDestaque"]
        )

    console = Console()
    console.print(tabela)