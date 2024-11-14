""" Trilha de Python - for_code [ ] - Exercícios -  Márcio Melchiades Nascimento """

class Padeiro:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.pao = 0
        self.pao_vendido = 0
        self.lucro = 0


    def fazer_pao(self, pao):
        self.pao = pao

class Cliente:
    def __init__(self, nome, idade, dinheiro):
        self.nome = nome
        self.idade = idade
        self.dinheiro = dinheiro
        self.comprado = 0

    def comprar_pao(self, padeiro):
        quantidade = int(input(f"\nQuantos pães o {self.nome} deseja comprar? "))
        preco = 0.5 * quantidade
        if padeiro.pao < quantidade:
            print(f"\nO padeiro {padeiro.nome} não possuí essa quantidade de pães.")
        else:
            if self.dinheiro >= preco:
                self.dinheiro -= preco
                self.comprado += quantidade
                padeiro.pao -= quantidade
                padeiro.pao_vendido += quantidade
                padeiro.lucro += preco
            else:
                print("Cliente sem dinheiro")