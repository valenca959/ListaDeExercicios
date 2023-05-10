num = int(input('Digite o número que deseja ver a tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i:^2} = {num * i}')
