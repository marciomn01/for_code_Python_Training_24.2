""" Trilha de Python  - for_code [ ] - Semana Zero -  Márcio Melchiades Nascimento """

# Feito com interaçaõ com o usuário

# Questão 1

#Intereaçao com o usuário
print("\nQuestão 1")
text = input("\nDigite o texto: ")
palavra = input("\nDigite a palavra a ser substituída: ")
substituta = input("\nDigite a palavra substituta: ")


def replac(text, palavra, substituta):
        
    text = text.replace(palavra, substituta)

    return text

print("\nQuestão 1")
print(replac(text, palavra, substituta))
print()


# Questão 2

#Intereaçao com o usuário
print("\nQuestão 2")
texto = input("\nDigite as figurinhas: ")


def figurinhas(texto):
    
    lista = texto.split(",")
    lista = sorted(lista)
    lista = ",".join(lista)


    return lista

print("\nQuestão 2")
print(figurinhas(texto))
print()
