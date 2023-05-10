num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
cont = 0
if num1 < num2:
    print('condição 1')
    for i in range(num1, num2+1):
        print(f'{i}')
        cont += i
else:
    for i in range(num1, num2-1, -1):
        print(f'{i}')
        cont -= i
print(f'A soma ou subtração(caso seja decrescente) = {cont}')
