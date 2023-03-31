while True:
    sexo = str(input('Escolha um sexo: [F/M] ')).upper().strip()
    if sexo in 'M':
        print('Você escolheu o sexo Masculino')
        break
    elif sexo in 'F':
        print('Você escolheu o sexo Feminino')
        break
    else:
        print('Sexo inválido, digite um sexo valido')
