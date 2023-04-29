num = int(input('Digite um número[0 a 999]: '))
num_aux = num

if num < 1000:
    centenas = num_aux // 100
    num_aux = num_aux % 100
    dezenas = num_aux // 10
    num_aux = num_aux % 10
    unidades = num_aux // 1

    if num >= 100:
        if centenas > 1:
            if dezenas > 1:
                if unidades > 1:
                    print(f'{num} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades.')
                else:
                    print(f'{num} = {centenas} centenas, {dezenas} dezenas e {unidades} unidade.')
            else:
                if unidades > 1:
                    print(f'{num} = {centenas} centenas, {dezenas} dezena e {unidades} unidades.')
                else:
                    print(f'{num} = {centenas} centenas, {dezenas} dezena e {unidades} unidade.')
        else:
            if dezenas > 1:
                if unidades > 1:
                    print(f'{num} = {centenas} centena, {dezenas} dezenas e {unidades} unidades.')
                else:
                    print(f'{num} = {centenas} centena, {dezenas} dezenas e {unidades} unidade.')
            else:
                if unidades > 1:
                    print(f'{num} = {centenas} centena, {dezenas} dezena e {unidades} unidades.')
                else:
                    print(f'{num} = {centenas} centena, {dezenas} dezena e {unidades} unidade.')
    elif 10 <= num < 100:
        if dezenas > 1:
            if unidades > 1:
                print(f'{num} = {dezenas} dezenas e {unidades} unidades')
            else:
                print(f'{num} = {dezenas} dezenas e {unidades} unidade')
        else:
            if unidades > 1:
                print(f'{num} = {dezenas} dezena e {unidades} unidades')
            else:
                print(f'{num} = {dezenas} dezena e {unidades} unidade')
    else:
        if unidades > 1:
            print(f'{num} = {unidades} unidades')
        else:
            print(f'{num} = {unidades} unidade')
else:
    print('O número informado é maior ou igual a mil')
