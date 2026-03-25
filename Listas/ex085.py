# Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separado os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

lista = [[], []]
num = 0

for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os números impares digitados foram: {lista[1]}')
print(f'Os números pares digitados foram: {lista[0]}')
