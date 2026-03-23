#Crie um programa que tenha uma palavras com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'THEO', 'MERCADO')
vogais = 'aeiou'
for p in palavras:
    print(f'\nNa palavra {p.upper()}  temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')