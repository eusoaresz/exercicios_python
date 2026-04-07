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
