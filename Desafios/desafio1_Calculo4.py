""" Trilha de Python  - for_code [ ] - Semana Um -  Márcio Melchiades Nascimento """

# Questão 1: Exercício Cálculo 4

# Importação da biblioteca math

from math import log, e

# Função para cálculo do somatório

def calculo():
    n = 2
    somatorio = 0  
    
    while True:
        somatorio += 1 / (n * log(n, e))
        n += 1
        print(somatorio)

calculo()