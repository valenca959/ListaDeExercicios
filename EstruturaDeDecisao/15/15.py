lado_a = float(input('Digite o 1° lado: '))
lado_b = float(input('Digite o 2° lado: '))
lado_c = float(input('Digite o 3° lado: '))
if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    if lado_a == lado_b and lado_b == lado_c:
        print('Triângulo Equilátero: três lados iguais')
    elif lado_a != lado_b != lado_c and lado_a != lado_c:
        print('Triângulo Escaleno: três lados diferentes')
    else:
        print('Triângulo Isósceles: quaisquer dois lados iguais')
else:
    print('Não foi possivel formar um triângulo')
