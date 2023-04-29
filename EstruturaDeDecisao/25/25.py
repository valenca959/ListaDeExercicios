print('Todas as respostas devem ser respondidas com sim ou não[S/N]')
telefone = str(input('Telefonou para a vítima? ')).strip()[0]
local = str(input('Esteve no local do crime? ')).strip()[0]
mora = str(input('Mora perto da vítima? ')).strip()[0]
devia = str(input('Devia para a vítima? ')).strip()[0]
trabalhou = str(input('Já trabalhou com a vítima? ')).strip()[0]

cont = 0
if telefone in 'Ss':
    cont = cont + 1
if local in 'Ss':
    cont = cont + 1
if mora in 'Ss':
    cont = cont + 1
if devia in 'Ss':
    cont = cont + 1
if trabalhou in 'Ss':
    cont = cont + 1
if cont == 2:
    print('SUSPEITA.')
elif 3 <= cont <= 4:
    print('CÚMPLICE.')
elif cont >= 5:
    print('ASSASSINO.')
else:
    print('INOCENTE.')
