from rich.console import Console
from rich.panel import Panel
import os

from operacoes.incluir import incluir
from operacoes.listar import listar
from operacoes.alterar import alterar
from operacoes.excluir import excluir
from operacoes.pesquisar import pesquisar

console = Console()

menu = ("""
1. Incluir Seleção
2. Listar Seleções
3. Pesquisar por ID
4. Alterar Seleção
5. Excluir Seleção
6. Finalizar
""")

while True:
#    console.clear()
    os.system("cls")
    console.print(Panel.fit(menu, title="Menu Principal"))

    opcao = int(input("Opção: "))

    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        alterar()
    elif opcao == 5:
        excluir()
    elif opcao == 6:
        console.print("[bold cyan]Fim do Programa[/bold cyan]")
        break
    else:
        console.print("[bold red]Opção inválida[/bold red]")

    input("\nPressione Enter para continuar...")