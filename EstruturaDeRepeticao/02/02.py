nome = str(input('Digite seu nome: ')).lower()
while True:
    senha = input('Digite sua senha: ')
    if senha.lower() == nome:
        print('Erro, a senha deve ser diferente do seu nome')
    else:
        break
