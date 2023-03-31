n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
maior = menor = n1
if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < n1:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O maior número digitado foi {maior} e o menor número foi {menor}')
