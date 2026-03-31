dados = {}
lista = []

dados['nome'] = str(input('Nome: '))
dados['partidas'] = int(input('Número de partidas: '))

total = 0

for c in range(0, dados['partidas']):
    gols = int(input(f'Quantos gols na partida {c+1}: '))
    lista.append(gols)
    total += gols
dados['gols'] = lista
dados['total'] = total

print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f' O campo {k} tem o valor {v}')
print('=-'*30)

print(f'O jogador {dados['nome']} jogou {dados['partidas']} partidas')

for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols')