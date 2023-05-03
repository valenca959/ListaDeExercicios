while True:
    nome = str(input('Digite seu nome: '))
    if len(nome) <= 3:
        print('Erro, nome menor ou igual a 3 caracteres')
    else:
        break
while True:
    idade = int(input('Digite sua idade: '))
    if 0 < idade > 150:
        print('Digite sua idade[entre 0 e 150]')
    else:
        break
while True:
    salario = float(input('Digite sua sálario: '))
    if salario <= 0:
        print('Valor invalido, digite novamente.')
    else:
        break
while True:
    sexo = str(input('Digite seu sexo: [F/M]')).strip()[0]
    if sexo not in 'FfMm':
        print('Erro, digite F para feminino e M para masculino.')
    else:
        break
while True:
    estado_civil = str(input('Estado Civil: [S/C/V/D]')).strip()[0]
    if estado_civil not in 'SsCcVvDd':
        print('Erro, S-Solteiro, C-Casado, V-Viuvo, D-divorciado')
    else:
        break
print('Cadastrado com sucesso!')
