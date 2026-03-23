#Gerar uma tupla preenchida com 5 números aleatórios entre 1 e 100. Exibir a lista de números sorteados. Usar um loop for para percorrer essa tupla e encontrar: Maior valor sorteado, menor valor sorteado

import random

tupla= tuple(random.randint(1, 100)for _ in range(0, 5))
print(f'Os números são: {tupla}')

menor = maior = tupla[0]

for n in tupla:
    if n < menor:
        menor = n
    if n > maior:
        maior = n
print(f'O maior é {maior}')
print(f'O menor é {menor}')