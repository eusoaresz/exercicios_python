import requests

from rich.console import Console
from rich.panel import Panel

from config import API_URL

def pesquisar():
    id = input("ID da seleção: ")

    resposta = requests.get(f"{API_URL}/{id}")

    if resposta.status_code != 200:
        print("Seleção não encontrada")
        return

    selecao = resposta.json()

    console = Console()

    texto = (
        f"Nome: {selecao['nome']}\n"
        f"Continente: {selecao['continente']}\n"
        f"Copas: {selecao['numCopas']}\n"
        f"Destaques: {selecao['destaques']}\n"
        f"Chance de Título: {selecao['chanceTitulo']}%"
    )

    console.print(
        Panel(texto, title="Dados da Seleção")
    )