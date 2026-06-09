# Exercícios Python - Algoritmos e Estrutura de Dados

Este projeto reúne exercícios práticos em Python para treinar lógica de programação, estruturas básicas e manipulação de dados por meio de pequenos jogos e desafios.

## Finalidade

- Praticar conceitos de algoritmos e estrutura de dados.
- Exercitar entrada e saída de dados no terminal.
- Desenvolver raciocínio lógico com problemas simples.

## Estrutura

- src/caca_niquel.py
- src/descubraPalavra.py
- src/forca.py
- src/jogo.py
- src/leitorSenha.py
- src/nomeAluno.py
- src/palavras.txt

## Requisitos

- Python 3 instalado.
- `colorama` instalado para cores no terminal (`src/jogo.py`).

## Instalação

No PowerShell (Windows), dentro da pasta raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install colorama
```

## Como executar

No terminal, estando na pasta raiz do projeto, rode um dos arquivos abaixo:

```powershell
python src/memoria.py
python src/jogo.py
python src/forca.py
python src/caca_niquel.py
python src/descubraPalavra.py
python src/leitorSenha.py
python src/nomeAluno.py
```

Se estiver usando ambiente virtual (opcional), ative antes de executar.

## Jogo de palavras (`src/jogo.py`)

- Lê as palavras de `src/palavras.txt`.
- Aceita chute de uma letra por vez.
- `*` mostra a dica e consome 1 vida.
- Exibe progresso no formato `Palavra: _ _ _ _`.
- As comparações são feitas em maiúsculo para contabilizar corretamente os acertos.

## Observações

- Os programas são independentes: execute um arquivo por vez.
- Alguns jogos usam emojis e limpeza de tela no terminal para melhorar a visualização.
- Se `colorama` aparecer sublinhado no editor, selecione no VS Code o mesmo interpretador Python do ambiente virtual ativo.

## Ambientes e erros comuns

- Ambientes virtuais: recomendo usar um `venv` por projeto. Para criar e ativar no PowerShell:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

- `ModuleNotFoundError: No module named 'colorama'`: instale no venv ativo:

```powershell
python -m pip install colorama
```

- Se o editor (Pylance) sublinhar uma importação, confirme que o VS Code está usando o mesmo Python do terminal: `Python: Select Interpreter`.

- `gitmoji` (CLI): o pacote correto é `gitmoji-cli`. Instale com `npm install -g gitmoji-cli`. Se o comando não for encontrado no terminal, adicione a pasta de binários do npm global ao `PATH` (Windows):

```powershell
setx PATH "$($env:PATH);$env:APPDATA\\npm"
```

- Caminho de arquivos (ex.: `palavras.txt`, `train.csv`): os scripts foram atualizados para localizar arquivos relative ao próprio arquivo (usa `Path(__file__)`). Ainda assim, rode os scripts a partir da raiz do projeto:

```powershell
python src/jogo.py
python src/titanic/titanic.py
```
