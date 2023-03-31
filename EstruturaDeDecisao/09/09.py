n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(f'Os números digitados foram {n1}, {n2} e {n3}')
    else:
        print(f'Os números digitados foram {n1}, {n3} e {n2}')
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(f'Os números digitados foram {n2}, {n1} e {n3}')
    else:
        print(f'Os números digitados foram {n2}, {n3} e {n1}')
else:
    if n1 >= n2:
        print(f'Os números digitados foram {n3}, {n1} e {n2}')
    else:
        print(f'Os números digitados foram {n3}, {n2} e {n1}')
