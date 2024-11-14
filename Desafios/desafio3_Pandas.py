""" Trilha de Python  - for_code [ ] - Semana Três -  Márcio Melchiades Nascimento """

# Questão 1: Utilize este csv para obter uma representação clara dos dados, por meio de gráficos ou outras funcionalidades do Pandas.

# Importação da biblioteca Pandas

import pandas as pd


# Leitura do arquivo csv

df = pd.read_csv("https://drive.usercontent.google.com/u/0/uc?id=16b6a7AQVldlJsqLOqF-HYDwSR_D3SuYr&export=download")

# Definição da função menu
def menu() -> str:
    """
    Está função exibe o menu de opções.

    params:: str

    return:: str
    """
    
    # Menu de opções
    print("\nBem-vindo a Leitura do mt.cars!")

    print("\n1 - Funções do Pandas")
    print("2 - Ver o DataFrame")
    print("3 - Data Science")
    print("4 - Créditos")
    print("5 - Sair\n")

    # Definição do dicionário de opções   
    dict_options = {
        "1": "functions",
        "2": "viewdf",
        "3": "DataScience",
        "4": "credits",
        "5": "exit"
    }

    # Loop para escolha da opção
    while True:
        resposta = input("Escolha uma opção: ")
        msg_erro = "Opção inválida! Insira um número de 1 a 4!"
        app_state = dict_options.get(resposta, msg_erro)
        if app_state != msg_erro:
            break
        print(msg_erro)


    return app_state

# Definição dos dicionários de funções e operações

dict_functions = {
    "\n1": "head()",
    "2": "tail()",
    "3": "info()",
    "4": "describe()",
    "5": "columns",
    "6": "shape",
    "7": "unique()",
    "8": "value_counts()",
    "9": "mean()",
    "10": "sum()",
    "11": "max()",
    "12": "min()",
    "13": "std()",
    "14": "corr()",
    "15": "groupby()",
    "16": "Sair\n"

}

dict_operations = {
    "1": lambda: (f"\nA função head() retorna as primeiras linhas de um DataFrame. Por padrão, retorna as 5 primeiras, mas é possível especificar um número diferente.\n\n{df.head(5)}\n"),
    "2": lambda: (f"\nA função tail() retorna as últimas linhas do DataFrame. Também exibe 5 por padrão, mas permite especificar a quantidade.\n\n{df.tail(5)}\n"),
    "3": lambda: (f"\nAfunção info() exibe um resumo sobre as colunas, tipo de dados, quantidade de valores não nulos e o uso de memória do DataFrame.\n\n{df.info()}\n"),
    "4": lambda: (f"\nA função describe() gera estatísticas descritivas como média, desvio padrão, mínimo, quartis e máximo para colunas numéricas.\n\n{df.describe()}\n"),
    "5": lambda: (f"\nO atributo columns retorna os nomes das colunas do DataFrame.\n\n{df.columns}\n"),
    "6": lambda: (f"\nO atributo shape retorna a forma do DataFrame como uma tupla.\n\n{df.shape}\n"),
    "7": lambda: (f"\nA função unique() retorna os valores únicos de uma coluna específica.\n\n{df['cyl'].unique()}\n"),
    "8": lambda: (f"\nA função value_counts() conta a frequência de cada valor único em uma coluna.\n\n{df['cyl'].value_counts()}\n"),
    "9": lambda: (f"\nA função mean() calcula a média aritmética dos valores de uma coluna em um DataFrame, nesse caso é a média dos cavalos.\n\n{df["hp"].mean()}\n"),
    "10": lambda: (f"\nA função sum() calcula a soma dos valores de uma coluna ou de todas as colunas numéricas se aplicado ao DataFrame inteiro.\n\n{df["hp"].sum()}\n"),
    "11": lambda: (f"\nA função max() retorna o valor máximo de uma coluna.\n\n{df['hp'].max()}\n"),
    "12": lambda: (f"\nA função min() retorna o valor mínimo de uma coluna.\n\n{df['hp'].min()}\n"),
    "13": lambda: (f"\nA função std() calcula o desvio padrão dos valores de uma coluna, nesse caso é dos cavalos.\n\n{df["hp"].std()}\n"),
    "14": lambda: (f"\nA função corr() calcula a correlação entre as colunas de um DataFrame\n\n1. 1 indica uma correlação positiva perfeita,\n2. -1 indica uma correlação negativa perfeita,\n3. 0 indica que não há correlação linear.\n\n{df[["cyl", "hp"]].corr()}\n"),
    "15": lambda: (f"\nA função groupby() permite agrupar dados com base em uma ou mais colunas e realizar operações agregadas, como soma, média, contagem, etc. É muito útil para análises categorizadas.\n\n{df.groupby('Unnamed: 0')["cyl"].mean()}\n"),
    "16": lambda: (back_to_menu())
}

#Definição da função menu_functions e menu_operations
def menu_functions() -> str:
    """
    Está função exibe o menu de funções do Pandas.

    params:: str

    return:: str
    """
    print("\n--- Funções do Pandas ---")
    for key, value in dict_functions.items():
        print(f"{key} - {value}")

    # Loop para escolha da opção
    while True:
        resposta = input("Escolha uma opção: ")
        msg_erro = "Opção inválida! Insira um número de 1 a 16!"
        if resposta in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]:
            break
        else:
            print(msg_erro)

    return resposta

def menu_operations(resposta: str) -> str:
    """
    Está função exibe as operações do Pandas.

    params:: str

    return:: str
    """
    global app_state
    
    if resposta != "16":
        print(dict_operations.get(resposta)())
    else:
        pass   
    app_state = back_to_menu()

    return resposta, app_state

#Definição da função Data Science
def data_science() -> str:
    """
    Está função exibe a análise de dados, que o usuário deseja realizar.

    params:: str

    return:: str
    """

    print("\n--- Bem vindo ao DataScience ---\n")
    
    for key, value in dict_functions.items():
        print(f"{key} - {value}")




# Definição da função back_to_menu
def back_to_menu() -> str:
    """
    Está função exibe a mensagem de retorno ao menu.

    params:: str

    return:: str
    """
    global app_state
    while True:
        resposta =input("\nPressione Enter para voltar ao menu...\n")
        msg_erro = "\nOpção inválida! Pressione Enter!"
        if resposta != "":
            print(msg_erro)
            
        else:
            app_state = "menu"
            break     
    return app_state


# Definição da função main
def main() -> None:
    """
    Está função é a principal do programa, onde será chamado o menu e as 
    opções escolhidas pelo usuário.

    params:: None

    return:: None
    """
    
    # Chamada da função menu
    app_state = menu()


    # Loop principal
    while True:
        match app_state:
            case "functions":

                resposta = menu_functions()
                chave = menu_operations(resposta)
                chave, app_state = chave

                
            case "viewdf":
                print("\nLeitura do arquivo csv: \n")
                print(f"{df}\n")
                
                app_state = back_to_menu()

            case "DataScience":

                print("\nData Science")

                app_state = back_to_menu()

            case "credits":
                print("\nDesenvolvido por: Márcio Melchiades Nascimento")
                print("Email: marciomelchiades.20221@poli.ufrj.br")
                print("GitHub: mahttps://github.com/marciomn01")
                print("LinkedIn: https://www.linkedin.com/in/marciomelchiadesnascimento/?originalSubdomain=br\n")
                
                app_state = back_to_menu()
            
            case "exit":
                print("\nObrigado por utilizar o meu leitor do mt.Cars! Até a próxima!\n")
                exit()

            case "menu":
                app_state = menu()


main()

"""
To do:

1. Functions 9, 13, 14, 15 | CHECK | Corrigido
2. Desenvolver a função Data Science | CHECK | Fazendo
3.
4.
5.

"""