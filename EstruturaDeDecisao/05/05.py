nota1 = float(input('Digite a 1° Nota: '))
nota2 = float(input('Digite a 2° Nota: '))
media = (nota1 + nota2) / 2
if media >= 10:
    print('APROVADO COM DISTINÇÂO!')
elif media >= 7:
    print('APROVADO!')
else:
    print('REPROVADO!')
