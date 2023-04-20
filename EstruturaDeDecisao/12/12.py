valor = float(input('Digite o valor ganho por horas: R$'))
horas = float(input('Digite a quantidade de horas trabalhadas: '))
desconto = 0
if 900 < horas * valor <= 1500:
    desconto = 5
elif 1500 < horas * valor <= 2500:
    desconto = 10
elif 2500 < horas * valor:
    desconto = 20

print(f'Salário Bruto:({valor} x {horas})    :R${valor * horas:.2f}'
      f'\n(-) IR    ({desconto})                  :R${(horas * valor * desconto) / 100:.2f}'
      f'\n(-) INSS  (10%)                :R${horas*valor*0.1:.2f}'
      f'\nFGTS (11%)                     :R${horas*valor*0.11:.2f}'
      f'\nTotal dos descontos            :R${horas*valor*(0.1+desconto/100):.2f}'
      f'\nSalário Liquido                :R${horas*valor*(1 -(0.1+desconto/100)):.2f}')
