""" Trilha de Python - for_code [ ] - Exercícios -  Márcio Melchiades Nascimento """

"""
    Ao definir um obj (Class Carro) é possivel atribuir atributos a ele (self), como marca, cavalos e modelo, e açoes a ele, como chamar_Carro e definir_Carro.
"""


class Carro:
    def __init__(self, marca, cavalos, modelo):
        self.marca = marca
        self.cavalos = cavalos
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def chamar(self) -> None:
        print(f"\nMarca: {self.marca} \nCavalos: {self.cavalos} \nModelo: {self.modelo}\n")

    def ligar(self) -> None:
        if self.ligado == False:
            self.ligado = True
            print("Carro ligado")
        else:
            print("Carro já está ligado")

    def desligar(self) -> None:
        if self.ligado == True:
            self.ligado = False
            print("Carro desligado")
        else:
            print("Carro já está desligado")

    def acelerar(self) -> int:
        if self.ligado == True:
            self.velocidade += 10
            print(f"Velocidade: {self.velocidade}")
        else:
            print("Carro desligado")

