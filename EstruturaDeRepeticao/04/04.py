populacaoA = 80000
populacaoB = 200000
ano = 0
while populacaoA <= populacaoB:
    crescimentoA = (3 * populacaoA) / 100
    crescimentoB = (1.5 * populacaoB) / 100
    populacaoA += crescimentoA
    populacaoB += crescimentoB
    ano += 1
print(f'Serão necesários {ano} anos.')
