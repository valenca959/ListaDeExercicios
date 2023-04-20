salario = float(input('Qual o valor do salário do colaborador: R$'))
percentual = 0
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5
reajuste = (salario * percentual) / 100
print(f'O salário antes do reajuste era de R${salario:.2f}\nCom o aumento de {percentual}%'
      f'\nHouve um aumento de R${reajuste} e o novo salário passou a ser R${salario + reajuste:.2f}')
