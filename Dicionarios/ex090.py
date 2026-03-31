dados = dict()

dados['nome'] = str(input('Nome: '))
dados ['media'] = float(input('Média: '))

if dados['media'] >= 7.0:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'

print(f'O aluno {dados["nome"]} com {dados["media"]} está {dados["situação"]}')