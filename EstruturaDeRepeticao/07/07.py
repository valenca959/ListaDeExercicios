maior = 0
for num in range(1,6):
    num = int(input(f'Informe o {num}° numero: '))
    if num > maior:
        maior = num
print(f'O maior número digitado foi {maior}')
