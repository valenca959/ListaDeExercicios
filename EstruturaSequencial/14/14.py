peso_peixe = float(input('Digite quantos Kg: '))
if peso_peixe <= 50:
    print(f'{peso_peixe}Kg de peixe não ultrapassou os 50Kg do regulamento, sem multa')
else:
    peso_excesso = peso_peixe - 50
    multa = peso_excesso * 4
    print(f'{peso_peixe}Kg de peixe \nUltrapassou {peso_excesso}Kg de peso e a multa foi de R${multa}')
