""" Trilha de Python - for_code [ ] - Exercícios -  Márcio Melchiades Nascimento """

import time as t
import os

def cronometro():

    segundos = 0
    minutos = 0
    horas = 0

    while True:
        os.system("cls")
        print(f"{horas}:{minutos:02}:{segundos:02}")
        t.sleep(1)
        segundos += 1
        if segundos == 60:
            minutos += 1
            segundos = 0
        if minutos == 60:
            horas += 1
            minutos = 0
        if horas == 24:
            break

cronometro()
