populacaoA = int(input('Digite a popululçao do País A: '))
taxaAnualA = float(input('Digite a taxa anual de crescimento do País: '))
populacaoB = int(input('Digite a população do País B: '))
taxaAnualB = float(input('Digite a taxa anual de crescimento do País: '))
ano = 0

while populacaoA <= populacaoB:
    crescimentoA = (taxaAnualA * populacaoA) / 100
    crescimentoB = (taxaAnualB * populacaoB) / 100
    populacaoA += crescimentoA
    populacaoB += crescimentoB
    ano += 1
print(f'Serão necesários {ano} anos.')
