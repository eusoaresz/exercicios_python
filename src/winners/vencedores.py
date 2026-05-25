#   A partir do arquivo winners.csv (kaggle.com) com os
#   pilotos vencedores de corridas da Fórmula 1, obter:
#   A lista dos 10 pilotos com maior nª de vitórias na
#   história da F1 (ordem decrescente de vitórias)
#   A lista das Equipes com 10 ou + vitórias na F1
#   (ordem crescente de vitórias)
#   A lista das 10 provas com vitórias com maior
#   tempo da F1 (ordem decrescente de tempo)
#   Tempo, Piloto, Equipe, GP e Data
#   Ler o nome de um Piloto. Se ele tiver vitórias,
#   listar os grandes prêmios que ele venceu.
#   Agrupar por ano e listar o número de corridas por
#   cada ano.

import csv

grupos = {}

with open('winners.csv', 'r') as file:
    reader = csv.DictReader(file)
    for winner in reader:
        grand_prix = winner['Grand Prix']
        date = winner['Date']
        pilot = winner['Winner']
        time = winner['Time']
        equipe = winner['Constructor']
        gp = winner['GP']
        code_name = winner['Code']

        if pilot not in grupos:
            grupos[pilot] = {
                'vitórias': 0,
                'equipes': set(),
                'gps': []
            }
        
        grupos[pilot]['vitórias'] += 1
        grupos[pilot]['equipes'].add(equipe)
        grupos[pilot]['gps'].append((gp, date, time))
    
# Lista dos 10 pilotos com maior número de vitórias
pilotos_vitoriosos = sorted(grupos.items(), key=lambda x: x[1]['vitórias'], reverse=True)[:10]
print("Top 10 Pilotos com maior número de vitórias:")
for piloto, info in pilotos_vitoriosos:
    print(f"{piloto}: {info['vitórias']} vitórias")