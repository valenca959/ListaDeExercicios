# Entrada de dados
dia = str(input("Digite o dia do mês: "))
mes = str(input('Digite o mês do ano: '))
ano = str(input('Digite o ano: '))

# Fatiamento e cálculo
if dia[0:2] != 0 and int(dia[0:2]) > 31:
    print('Data Inválida')
else:
    if mes[0:2] !=0 and int(mes[0:2]) > 12:
        print('Data Inválida')
    else:
        if ano[0:4] != 0 and int(ano[0:4]) > 9999:
            print('Data Inválida')
        else:
            print(f'Você digitou a data {dia}/{mes}/{ano}.')
