dinheiro = int(input('Digite o valor para saque [mínimo 10\máximo 600]: R$'))
din_aux = dinheiro
nota_cem = nota_ciquenta = nota_vinte = nota_cinco = nota_um = 0
if 10 <= dinheiro <= 600:
    if dinheiro > 100:
        # Retirar as notas de 100
        nota_cem = dinheiro // 100
        din_aux = din_aux % 100
        # Retirar as notas de 50
        nota_ciquenta = din_aux // 50
        din_aux = din_aux % 50
        # Retirar as notas de 20
        nota_vinte = din_aux // 20
        din_aux = din_aux % 20
        # Retirar as notas de 5
        nota_cinco = din_aux // 5
        din_aux = din_aux % 5
        # Retirar as notas de 1
        nota_um = din_aux // 1
        din_aux = din_aux % 1
    if nota_cem > 0:
        print(f'R${nota_cem} notas de cem')
    if nota_ciquenta > 0:
        print(f'R${nota_ciquenta} notas de ciquenta')
    if nota_vinte > 0:
        print(f'R${nota_vinte} notas de vinte')
    if nota_cinco > 0:
        print(f'R${nota_cinco} notas de cinco')
    if nota_um > 0:
        print(f'R${nota_um} notas de um')
print(f'Valor sacado ao total {dinheiro}')
