print('o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.')
combustivel = str(input('Gostaria de abastecer com A-Álcool ou G-Gasolina: ')).strip()[0]
litros = int(input('Informe quantos litros deseja: '))
desconto = preco = 0

if combustivel in 'Aa':
    preco = 1.90
    if litros <= 20:
        desconto = (3 * litros * preco) / 100
    else:
        desconto = (5 * litros * preco) / 100
if combustivel in 'Gg':
    preco = 2.5
    if litros <= 20:
        desconto = (4 * litros * preco) / 100
    else:
        desconto = (6 * litros * preco) / 100
print(f'O valor total é de R${(litros * preco) - desconto}')
