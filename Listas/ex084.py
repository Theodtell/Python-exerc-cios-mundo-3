# Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) uma listagem com as pessoas mais leves

temp = []
princ = []
total_cadastros = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    while True:
        resp = str(input('Quer continua? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=-'*30)

# A) Quantas pessoas foram cadastradas

print(f'Você cadastrou {len(princ)} pessoas')

# B) Uma listagem com as pessoas mais pesadas

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{[p[0]]} ', end='')
print()

#C) uma listagem com as pessoas mais leves

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{[p[0]]} ', end='')
print()