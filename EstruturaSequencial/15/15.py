valor_horas = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas trabalhadas no mês? '))
salario_bruto = valor_horas * horas
desconto_IR = (salario_bruto * 11) / 100            # IR        (11%)
desconto_INSS = (salario_bruto * 8) / 100           # INSS      (8%)
desconto_sindicato = (salario_bruto * 5) / 100      # Sindicato (5%)
descontos = desconto_IR + desconto_INSS + desconto_sindicato
salario_liquido = salario_bruto - descontos
print(f'O Salário Bruto é de R${salario_bruto:.2f}, Descontado R${descontos:.2f}')
print(f'- IR 5% R${desconto_IR:.2f} \n- INSS 8% R%{desconto_INSS:.2f} \n- Sindicato 5% R%{desconto_sindicato:.2f}')
print(f'O Salário Liquido é de R${salario_liquido:.2f}')
