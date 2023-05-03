while True:
    numero = int(input('Digite um número de 0 a 10: '))
    if 0 <= numero <= 10:
        break
    else:
        print('valor válido')
print(f'Você digitou {numero}')
