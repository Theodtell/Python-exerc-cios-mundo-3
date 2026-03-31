"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os pessoa de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""
pessoa = {}
galera = []
soma = 0

#recebe os jogador
while True:
    pessoa.clear() #limpa o dicionário para receber novos jogador
    pessoa['nome'] = str(input('Nome: '))
    #validação do sexo
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy()) #cópia do dicionário para uma lista
    #validação do continuar
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)

#A) Quantas pessoas foram cadastradas
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')

#B) A média de idade do grupo
media =  soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')

#C) Uma lista com todas as mulheres
print(f'As mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'- {p["nome"]} ')

#D) Uma lista com todas as pessoas com idade acima da média
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'- {k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')