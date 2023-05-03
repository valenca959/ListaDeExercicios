num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 < num2:
    for i in range(num1, num2):
        print(f'{i}')
else:
    for i in range(num1, num2, -1):
        print(f'{i}')
