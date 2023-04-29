nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
    print(f'APROVADO COM DISTINÇÂO, MÈDIA 10 PARABENS. ')
elif media >= 7:
    print(f'APROVADO!, a  média foi de {media} pontos.')
else:
    print(f'REPROVADO, a média foi de {media} pontos.')
