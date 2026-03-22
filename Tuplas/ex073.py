#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre: A) apenas os 5 primeiros colocados ; B) os ultimos 4 colocados; C) uma lista com os times em ordem alfabetica; D) em que posição na tabela está o time da Chapecoense

times = 'Palmeiras', 'São Paulo', 'Bahia', 'Flamengo', 'Fluminense', 'Coritiba', 'Grêmio', 'Athelico-PR', 'Corinthians', 'Vasco da Gama', 'Atlético-MG', 'Bragantino', 'EC Vitória', 'Chapecoense', 'Mirassol', 'Santos', 'Internacional', 'Botafogo', 'Cruzeiro', 'Remo'
print(20*'=-')
print(f'Lista de times do Brasileirão: {times}')
print(20*'=-')
#A) Apenas os 5 primeiros colocados
print(f'Os 5 primeiros são: {times[0:5]}')
print(20*'=-')
#B) os ultimos 4 colocados
print(f'Os 4 últimos são: {times[-4:]}')
print(20*'=-')
#C) uma lista com os times em ordem alfabetica
print(f'Times em ordem alfabética: {sorted(times)}')
print(20*'=-')
#D) em que posição na tabela está o time da Chapecoense
print(f'O time Chapecoense está na posição {times.index('Chapecoense')+1}°')
print(20*'=-')