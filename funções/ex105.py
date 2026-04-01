def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vário alunos
    :param n: Uma ou mais notas de alunos
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'BOA'
        elif 6 <= r ['media'] < 7:
            r['situaçao'] = 'RAZOÁVEL'
        else:
            r['situaçao'] = 'RUIM'
    return r

#programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=False)
print(resp)