from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
ano_atual = date.today().year
dados['idade'] = ano_atual - dados['idade']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - ano_atual
else:
    print(dados)

print('-=' * 30)
for k, v in dados.items():
        print(f'- {k} tem o valor {v}')