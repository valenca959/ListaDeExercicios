n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número digitado foi {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número digitado foi {n2}')
else:
    print(f'O maior número digitado foi {n3}')
