import csv
visitantes = []

with open("visitors_japan.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    visitantes.append(linha)

# print(visitantes[0])
# print(visitantes[0]['Country'])

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def num_paises():
  titulo("Número de Países Analisados")
  paises = set()
  for visitante in visitantes:
    paises.add(visitante['Country'])

    numero_paises = len(paises)
  print(f"Número de países analisados: {numero_paises}")

  #-----------List comprehension----------------
  numero2 = len(set(visitante['Country'] for visitante in visitantes))
  print(f"Número de países analisados (list comprehension): {numero2}")

def top10_paises():
  titulo("Top 10 Países com Maior Nº de Visitantes")

  grupos = {}

  for visitante in visitantes:
    pais = visitante['Country']
    num = int(visitante['Visitor'])
    #grupos.get() obtem o valor da chave pesquisada ou 0 se nap existir
    grupos[pais] = grupos.get(pais, 0) + num

    # print(grupos.items())

    grupos2 = dict(sorted(grupos.items(), key=lambda item: item[1], reverse=True))

  print("N País...........................Nº Visitantes")
  print("-"*40)

  for x, (pais, num) in enumerate(grupos2.items(), start=1):
    print(f"{x:2d} {pais:30s} {num:13d}")
    if x == 10:
      break


while True:
  titulo("Visitantes do Japão - Análise de Dados")
  print("1. N de Países analisados")
  print("2. Top 10 + paises com maior Nº de visitantes")
  print("3. Países com +100 mil / mês")
  print("4. Compara Top 10 de um ano com Geral")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    num_paises()
  elif opcao == 2:
    top10_paises()
  elif opcao == 3:
    analise_classe()
  else:
    break
