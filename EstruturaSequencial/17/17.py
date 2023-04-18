area = float(input('Digite o tamanho da área: '))
excesso = area - int(area)  # Salvando as casas decimais da area
area = int(area)  # Aqui retiramos a parte inteira da area
if excesso > 0:
    area += 1
litros = area // 6
if area % 6 > 0:
    litros += 1
print(f'Litro(s) necessários: {litros}L\n')
latas = litros // 18
if litros % 18 > 0:
    latas += 1
print('\033[1;36mcomprar apenas latas de 18 litros\033[m')
print(f'Serão necessárias {latas} latas'
      f'\nTeremos {latas * 18} litros'
      f'\nTotal: R${latas * 80}\n')

galoes = litros // 3.6
if litros % 3.6 > 0:
    galoes += 1
print('\033[1;36mcomprar apenas galões de 3,6 litros\033[m')
print(f'Serão necessários {galoes} galões'
      f'\nTeremos {galoes * 3.6} litros'
      f'\nTotal: R${galoes * 25}\n')

latas = litros // 18
litros_restantes = litros % 18
if litros_restantes <= 3 * 3.6:
    galoes = litros_restantes // 3.6
    if litros_restantes % 3.6 > 0:
        galoes += 1
print('\033[1;36mmisturar latas e galões\033[m')
print(f'Serão necessárias {latas} latas'
      f'\nSerão necessários {galoes} galões'
      f'\nObteremos {(latas * 18) + (galoes * 3.6)} litros'
      f'\nTotal: R${(latas * 80) + (galoes * 25)}')
