def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            nreal = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return nreal

#programa principal
nInteiro = leiaint('Digite um número inteiro: ')
nReal = leiafloat('Digite um número Real: ')
print(f'Você acabou de digitar o número {nInteiro}')
print(f'Você acabou de digitar o número {nReal}')