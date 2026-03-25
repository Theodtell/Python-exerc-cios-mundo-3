# crie um programa que vai ler vário números e colocar em uma lista. Depois disso, crie duas lista extras que vão conter apoenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

lista_geral = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um valor: '))
    lista_geral.append(num)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('Não entendi, ', end='')
    if opcao == 'N':
        break
for item in lista_geral:
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)
print(f'Você digitou os seguintes valores {sorted(lista_geral)}')
print(f'Lista par: {sorted(lista_par)}')
print(f'Lista impar: {sorted(lista_impar)}')