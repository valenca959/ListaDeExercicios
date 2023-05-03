soma = media = 0
for num in range(1, 6):
    num = int(input(f'Informe o {num}° numero: '))
    soma += num
media = soma / 5
print(f'A média é = {media} e a soma é = {soma}')
