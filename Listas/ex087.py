#Aprimore o desafio anterior, mostrando no final: A) a soma de todos os valores pares, B) a soma dos valores da terceira coluna e C) o maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0

#montando a matriz
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:  '))
print('='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()

# A) a soma de todos os valores pares
print(f'A soma de toda a matriz foi {soma_pares}')
# B) a soma dos valores da terceira coluna
soma_coluna = 0
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma da coluna 3 foi: {soma_coluna}')

# C) o maior valor da segunda linha
print(f'O maior valor digitado na linha 2 foi: {max(matriz[1])}')