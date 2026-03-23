#Crie um programa que tenha uma palavras única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print(40*'-')
print(f'{'LISTAGEM DE PREÇOS':^40}')
print(40*'-')

listagem = ('Lápis', 1.75, 'Borracha', 2,'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for pos in range (0, len(listagem)):
    if pos % 2 == 0: #aqui vai pegar apenas o nome dos produtos, pois ficam na posição par
        print(f'{listagem[pos]:.<30}', end='') #<30 coloca 30 caracteres
    else:
        print(f'R$ {listagem[pos]:>6.2f}')
print(40*'-')

