#Crie um programa que vai gerar cinco números aleatórios e colocar em uma palavras. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na palavras.
import random

maior = 0
menor = 1

numeros = tuple(random.randint(1,10) for _ in range(5))
print(f'Os valores sorteados foram: ', end='')

for numero in numeros:
    print(f'{numero} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}\nO menor valor sorteado foi: {min(numeros)}')