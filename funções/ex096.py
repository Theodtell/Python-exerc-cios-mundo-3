def area (l, c):
    retangulo = l * c
    print(f'A área de um terreno {l}X{c} é de {retangulo}m².')


print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)