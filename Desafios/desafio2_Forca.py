""" Trilha de Python  - for_code [ ] - Semana Dois -  Márcio Melchiades Nascimento """

# Questão 1: Fazer uma Forca com o Python.


# Importação da biblioteca random

import random as rd

# Definição da função

def forca() -> None:
    """
    Está função é um jogo de forca, onde o jogador tem que adivinhar a palavra secreta.

    Imput:: str

    output:: str
    """
    # Mensagem de boas vindas
    print("\nBem vindo ao jogo da Forca!")

    # Definição das palavras possíveis

    palavras = ["Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "HTML", "CSS", "SQL", "R", "Matlab", "C#", "Swift", "Kotlin", "Go", "Perl", "Lua", "Scala", "Rust", "Haskell", "Elixir", "Erlang", "Clojure", "F#", "Dart", "TypeScript", "Assembly", "COBOL", "Fortran", "Pascal", "Lisp", "Prolog", "Ada", "Logo", "Scratch", "Alice", "Scheme", "Smalltalk", "Simula", "Modula", "Simulink", "LabView", "Verilog", "VHDL", "SystemVerilog", "Ada", "Bash", "PowerShell", "Zsh", "Fish", "Tcsh", "Ksh", "Csh", "Sh", "AWK", "Sed", "Makefile", "Racket", "Julia", "Groovy", "Objective-C", "Objective-C++", "ActionScript", "ColdFusion", "D", "Dart", "Delphi", "Eiffel"]

    # Lista com as letras escolhidas

    letra_escolhida = []
    
    
    # Definição da quantidade de erros

    erros = 10

    # Definição da palavra secreta

    palavra_secreta = rd.choice(palavras)

    while True:
        # loop para rodar o jogo enquanto não acabar os erros
        
        # Escolha da letra

        tentativa = input("\n\nEscolha uma letra: ")
        letra_escolhida.append(tentativa)

        # Apenas visual
        print("\nA palavra secreta é: ")

        # Loop para verificar se a letra escolhida está na palavra secreta
        for letra in palavra_secreta:
            if letra in letra_escolhida:
                print(letra, end=" ") 
            else:
                print("_", end=" ")                                
        
        # Condições de vitória

        if all(letra in letra_escolhida for letra in palavra_secreta):
            print(f"\n\nVocê venceu! A palavra secreta era: {palavra_secreta}\n")
            break

        # Condições de derrota e erro
        if tentativa not in palavra_secreta:
            erros -= 1
            print(f"\n\nVocê errou! Restam {erros} tentativas.")
        
        if erros <= 0:
            print(f"\nVocê perdeu! A palavra secreta era: {palavra_secreta}\n")
            break   


forca() # Chamada da função
