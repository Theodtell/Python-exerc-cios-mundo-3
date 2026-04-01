from time import sleep

def maior(*num):
    cont = maior_num = 0
    print('-=' * 30)
    print('Analisando os valores passados...')

    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior_num = valor
        else:
            if valor > maior_num:
                maior_num = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior_num}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()
