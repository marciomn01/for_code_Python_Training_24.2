try:
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))

    r = x / y
    print(r)
except ZeroDivisionError:
    print('Divisão por zero')
except ValueError:
    print('Valor inválido')
except Exception as erro:
    print('O erro foi Erro:', erro)
else:
    print('Tudo certo')
finally:
    print('Fim do programa')
