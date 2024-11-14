# Adicione o nome das pessoas responsáveis por resolver esta questão Breno Affonso, Márcio e Wesley.

# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leitura dos dados a partir de um arquivo CSV hospedado no Google Sheets
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRs7pvsnOP8c3vXnk_UL9H5wLmwDTuY9arGK9zEWoGIe02BaqOWLE2VbS-00F43vMp5sj1N7Q6pYi71/pub?gid=0&single=true&output=csv')

# Remoção da coluna 'dados aleatorios'
df = df.drop(columns=['dados aleatorios'])

# Adição de uma coluna 'Tempo' com valores de 0 até o tamanho do DataFrame
df['Tempo'] = range(0, len(df))

# Remoção de linhas com valores NaN nas colunas 'Concentração (mol/L)' e 'pH'
df = df.dropna(subset=['Concentração (mol/L)'])
df = df.dropna(subset=['pH'])

# Criação do primeiro gráfico: Tempo vs Concentração (mol/L)
plt.figure(1)
plt.figure(figsize=(10, 6))  # Opcional: definir o tamanho do gráfico
plt.plot(df['Tempo'], df['Concentração (mol/L)'], marker='o', linestyle='-')
plt.title('Tempo vs Concentração (mol/L)')
plt.xlabel('Tempo')
plt.ylabel('Concentração (mol/L)')
plt.ylim(0, 0.2)
plt.grid(True)

# Função para criar gráficos com base em eixos e limites fornecidos
def graphSet(xAxis, yAxis, upperLim, lowerLim, figNum):
    # Cálculo da média geral agrupada pelo eixo x
    mediaGeral = df.groupby(xAxis)[yAxis].mean().reset_index()

    # Criação do gráfico
    plt.figure(figNum)
    plt.figure(figsize=(10, 6))
    plt.plot(mediaGeral[xAxis], mediaGeral[yAxis], marker='o')
    plt.title(f'{xAxis} vs {yAxis}')
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.ylim(lowerLim, upperLim)
    plt.grid(True)

# Criação de gráficos adicionais usando a função graphSet
graphSet('pH', 'Concentração (mol/L)', 0.2, 0, 2)
graphSet('Temperatura (°C)', 'Concentração (mol/L)', 0.2, 0, 2)
graphSet('Temperatura (°C)', 'pH', 6, 8, 2)

# Cálculo de estatísticas descritivas
ConcMedia = df['Concentração (mol/L)'].mean()
ConcMax = df['Concentração (mol/L)'].max()
ConcMin = df['Concentração (mol/L)'].min()

# Identificação dos tempos correspondentes à concentração máxima e mínima
maxTempo = df.loc[df['Concentração (mol/L)'].idxmax(), 'Tempo']
minTempo = df.loc[df['Concentração (mol/L)'].idxmin(), 'Tempo']

# Cálculo da variação média e do desvio padrão da concentração
variacaoMedia = df['Concentração (mol/L)'].diff().mean()
desvioPadrao = df['Concentração (mol/L)'].std()

# Impressão dos resultados
print(f'Concentração média é {ConcMedia} mol/l')
print(f'Concentração máxima: {ConcMax} mol/l, ocorreu em {maxTempo} minutos')
print(f'Concentração mínima em {ConcMin} mol/l, ocorreu em {minTempo} minutos')
print()
print(f'Variação média da concentração é {variacaoMedia} e o desvio padrão é {desvioPadrao}')

# Exibição dos gráficos
plt.show()
