letra = input('Digite uma letra: ').upper().strip()
if letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
    print(f'A letra {letra} é consoante')
else:
    print(f'A letra {letra} é vogal')
