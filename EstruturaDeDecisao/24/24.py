num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
opc = int(input('1 -- SOMAR\n'
                '2 -- SUBTRAIR\n'
                '3 -- MULTIPLICAR\n'
                '4 -- DIVIDIR\n'
                'Digite sua opção: '))
resultado = 0
if opc == 1:
    resultado = num1 + num2
    print(f'O resultado da soma {num1} + {num2} = {resultado:.2f}')
elif opc == 2:
    resultado = num1 - num2
    print(f'O resultado da subtração {num1} - {num2} = {resultado:.2f}')
elif opc == 3:
    resultado = num1 * num2
    print(f'O resultado da multiplicação {num1} x {num2} = {resultado:.2f}')
elif opc == 4:
    resultado = num1 / num2
    print(f'O resultado da divisão {num1} ÷ {num2} é {resultado:.2f}')
else:
    print('OPÇÂO INVALIDA')
if resultado % 2 == 0:
    print(f'{resultado} é PAR,', end=' ')
else:
    print(f'O resultado {resultado} é IMPAR,', end=' ')
if resultado > 0:
    print('é positivo', end=' ')
else:
    print('é negativo', end=' ')
if resultado - int(resultado) == 0:
    print('e ele é inteiro.')
else:
    print('e ele é negativo.')
