# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

dados = {}

dados['nome'] = str(input('Nome: '))
dados ['media'] = float(input('Média: '))

if dados['media'] >= 7.0:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'

print(f'O aluno {dados["nome"]} com {dados["media"]} está {dados["situação"]}')