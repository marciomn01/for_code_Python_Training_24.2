def df():

    while True:
        try:
            resposta = int(input('Digite um número: '))
            break
        except ValueError:
            print('Digite um número inteiro!')
        
    return resposta

print(df()*2)