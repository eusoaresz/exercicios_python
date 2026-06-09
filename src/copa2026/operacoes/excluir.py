import requests

from rich import print

from config import API_URL

def excluir():
    id = input("ID da seleção: ")

    resposta = requests.delete(f"{API_URL}/{id}")

    if resposta.status_code in [200, 204]:
        print("[green]Registro excluído![/green]")
    else:
        print("[red]Erro ao excluir[/red]")