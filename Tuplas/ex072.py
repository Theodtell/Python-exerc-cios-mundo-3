#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    opcao = ''
    while True:
        valor = int(input('Digite um número entre 0 e 20: '))
        if 0 <= valor <= 20:
            break
        print('Tente novamente.', end='')
    print(f'Você digitou o número {cont[valor]}')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        print('Não entendi',end='')
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break