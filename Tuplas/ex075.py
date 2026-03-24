# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma palavras. No final, mostre: A) quantas vezes apareceu o numero 9. B) em que posição foi digitado o primeiro valor 3 ; C) quais foram os números pares

numeros_lista = []

for c in range(1, 5):
    num = int(input(f'Digite o {c}° número: '))
    numeros_lista.append(num) #adiciona os números digitados na lista

# convertendo de lista para tuplas
tupla = tuple(numeros_lista)

#A) quantas vezes apareceu o numero 9
if 9 in tupla:
    print(f'O valor 9 aparece {tupla.count(9)} vezes')
else:
    print('Não foi digitado o valor 9.')
#B) em que posição foi digitado o primeiro valor 3
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}° posição')
else:
    print('Não foi digitado o número 3')
#C) quais foram os números pares
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')