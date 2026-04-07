import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos o valor de {moeda.aumentar(p,10)}')
print(f'Diminuindo 13%, temos o valor de {moeda.diminuir(p,13)}')