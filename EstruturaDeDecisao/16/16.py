a = float(input('Digite o valor de a: '))
if a >0:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    delta = b**2 - 4 * a * c

    if delta < 0:
        print('Não há raízes reais')
    elif delta == 0:
        print(f'Há apenas uma raíz real igual a {-b/(2*a)}')
    else:
        print('Há duas raízes: ')
        print(f'Raíz 1: {(-b+delta**(1/2))/(2*a)}')
        print(f'Raíz 2: {(-b-delta**(1/2))/(2*a)}')
else:
    print('A equação não é do segundo grau')
