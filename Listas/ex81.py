#crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados, B) a lista de valores ordenada de forma decrescente. C) se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('Não entendi, ', end='')
    if opcao == 'N':
        break
# A) Quantos números foram digitados
print(f'Foram digitados {len(lista)} números na lista')
# B) a lista de valores ordenada de forma decrescente
print(f'Os números digitados em ordem crescente foram {sorted(lista)}')
# C) se o valor 5 foi digitado e está ou não na lista
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista')
