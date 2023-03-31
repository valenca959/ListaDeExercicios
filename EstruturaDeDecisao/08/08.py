n1 = float(input('Digite o preço do 1° produto: '))
n2 = float(input('Digite o preço do 2° produto: '))
n3 = float(input('Digite o preço do 3° produto: '))
produto = n1
if produto > n2:
    produto = n2
    if produto > n3:
        produto = n3
print(f'O valor do produto mais barato foi de R${produto:.2f}')
