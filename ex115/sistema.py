from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

from ex115.lib.interface import leiaint

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Listar pessoas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resp == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRADO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1)