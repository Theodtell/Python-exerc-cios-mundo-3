galera = []
dado = []

for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() # limpa a lista
for item in galera:
    print(f'{item[0]} tem {item[1]} anos.')