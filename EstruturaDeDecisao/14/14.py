nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
media = (nota_1 + nota_2) / 2
print(f'A média entre {nota_1} e {nota_2} = {media},', end=' ')
if media >= 9:
    print('Aproveitamento A')
    print('APROVADO!')
elif media >= 7.5:
    print('Aproveitamento B')
    print('APROVADO!')
elif media >= 6:
    print('Aproveitamento C')
    print('APROVADO!')
elif media >= 4:
    print('Aproveitamento D')
    print('REPROVADO!')
else:
    print('Aproveitamento E')
    print('REPROVADO!')
