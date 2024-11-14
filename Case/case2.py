'''  Processo Seletivo 2024.2 - for_code [ ] - Case 2: Série de Taylor'''

# Importar as bibliotecas necessárias

import matplotlib.pyplot as plt
import numpy as np
import math

# Definir as funções

def taylor_exp(x, n):
    result = 0
    for i in range(n + 1):
        result += (x ** i) / math.factorial(i)
    return result


# Criar um array de valores x
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calcular os valores y para cada função
yExp=np.exp(x)
yTaylor3 = taylor_exp(x, 3)
yTaylor6 = taylor_exp(x, 6)


# Plotar as funções
plt.plot(x, yExp, label='exp(x)')
plt.plot(x, yTaylor3, label='P3(x)')
plt.plot(x, yTaylor6, label='P6(x)')

plt.xlim([-3, 3])
plt.ylim([0, 10])
plt.grid(True)

# Adicionar título e legendas
plt.title('Gráfico de funções')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostrar o gráfico
plt.show()