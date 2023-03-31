turno = str(input('Digite o turno que você estuda: [M/V/N] ')).strip()[0]
if turno in 'Mm':
    print('Bom Dia!')
elif turno in 'Vv':
    print('Boa Tarde!')
elif turno in 'Nn':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
