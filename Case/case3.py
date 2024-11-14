'''  Processo Seletivo 2024.2 - for_code [ ] - Case 3: Monitor de Pixels'''

# Importar as bibliotecas necessárias

import random


# Solicitar ao usuário os valores de linha, coluna e pixels

linha = int(input("\nDigite o número de linhas: "))
coluna = int(input("Digite o número de colunas: "))
pixels = int(input("Digite a porcentagem de pixels acesos: "))


# Definir a função monitor

def monitor(linha, coluna, pixels):
    sum = linha * coluna
    
    # Calcular a quantidade de 1s e 0se
    qnt_1s = int((pixels / 100) * sum)
    qnt_0s = sum - qnt_1s

    # Preencher lista_mae com valores aleatórios entre 0 e 1
    lista_mae = [1] * qnt_1s + [0] * qnt_0s
    

    # Embaralhar lista_mae
    random.shuffle(lista_mae)
    
    
    # Dividir lista_mae em sublistas de acordo com o número de colunas
    lista_nova = [lista_mae[i:i + coluna] for i in range(0, sum, coluna)]
    
    return lista_mae, lista_nova

# Chamar a função e armazenar os resultados em variáveis
lista_mae, lista_nova = monitor(linha, coluna, pixels)

# Imprimir as listas resultantes
print("\nMonitor:\n")
for i in lista_nova:
    print(i)
