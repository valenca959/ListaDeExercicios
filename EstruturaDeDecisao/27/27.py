morango = float(input("Digite a quantidade de morango(kg): "))
maca = float(input("Digite a quantidade de maçã(kg): "))
total = 0

if morango > 5:
    total += morango*2.2
else:
    total += morango*2.5

if maca > 5:
    total += maca * 1.5
else:
    total += maca * 1.8

if total > 25:
    total *= 0.9

print(f"Total a ser pago: R${total:.2f}")
