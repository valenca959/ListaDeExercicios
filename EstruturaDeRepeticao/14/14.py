impa = pares = 0
for i in range(1, 11):
    num = int(input(f'Digite o {i}° Número: '))
    if num % 2 == 0:
        pares += 1
    else:
        impa += 1
print(f'foram digitados {pares} números pares e {impa} números impares.')
