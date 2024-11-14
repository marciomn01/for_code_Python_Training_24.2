""" Trilha de Python - for_code [ ] - Exercícios -  Márcio Melchiades Nascimento """

from Classes_padaria import Padeiro
from Classes_padaria import Cliente


# Instanciando objetos
padeiro1 = Padeiro("João", 30, 1000)
cliente1 = Cliente("Maria", 25, 100)
padeiro2 = Padeiro("José", 35, 1500)
cliente2 = Cliente("Joana", 20, 100)


# Chamando métodos

padeiro1.fazer_pao(5)
print(f"\nO padeiro {padeiro1.nome} produziu {padeiro1.pao} pães.")
cliente1.comprar_pao(padeiro1)
print(f"\nO padeiro {padeiro1.nome} vendeu {padeiro1.pao_vendido} pães.")
print(f"O padeiro {padeiro1.nome} possuí {padeiro1.pao} pães restantes.") 
print(f"O padeiro {padeiro1.nome} lucrou {padeiro1.lucro} reais com a venda de pães.")
print(f"O Cliente {cliente1.nome} comprou {cliente1.comprado} pães.")
print(f"O Cliente {cliente1.nome} possuí {cliente1.dinheiro} reais.\n")

