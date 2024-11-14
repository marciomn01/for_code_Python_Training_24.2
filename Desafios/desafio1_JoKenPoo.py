""" Trilha de Python  - for_code [ ] - Semana Um -  Márcio Melchiades Nascimento """

# Questão 1: Fazer um pedra, papel, tesoura, lagarto e Spok.

# Importação da biblioteca random e time

import random as rd
import time as tm

# Definição da função

def TheBigBangJoKenPo():
    
    # Definição das opções possíveis

    escolhas = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spok"]

    # Definição da quantidade de rodadas

    win_player = 0
    win_npc = 0
    empate = 0

    # Loop para a quantidade de rodadas
    
    while True:
        
        # Escolha do jogador e do NPC

        player_choice = input("\nEscolha entre pedra, papel, tesoura, lagarto e Spok: ")
        player_choice = player_choice.capitalize()
        npc_choice = rd.choice(escolhas)
        
        print() # Pular linha
        
        # Mensagem de JO KEN PO
        tm.sleep(0.5)
        for i in escolhas:
            tm.sleep(0.3)
            print(i)
        tm.sleep(0.5)
        
        # Mensagem de escolha
        print(f"\nJogador: {player_choice} ")
        print(f"NPC: {npc_choice}\n")

        # Condições de Empate

        if player_choice == npc_choice:
            print("Empate, parece que nos conhecemos bem!")
            empate += 1
            if empate == 2:
                print("Bazinga! Empate duplo, vamos recomeçar!")
                empate += 1
            elif empate >= 3:
                print("Por favor, escolha uma opção diferente! AAAAH!")
                empate = 0

        # Condições de Vitória

        elif player_choice == "Tesoura" and npc_choice == "Papel":
            print("Tesoura corta Papel!")
            win_player += 1

        elif player_choice == "Papel" and npc_choice == "Pedra":
            print("Papel cobre Pedra!")
            win_player += 1
        
        elif player_choice == "Pedra" and npc_choice == "Lagarto":
            print("Pedra esmaga Lagarto!")
            win_player += 1
        
        elif player_choice == "Lagarto" and npc_choice == "Spok":
            print("Lagarto envenena Spok!")
            win_player += 1
        
        elif player_choice == "Spok" and npc_choice == "Tesoura":
            print("Spok amassa Tesoura!")

        elif player_choice == "Tesoura" and npc_choice == "Lagarto":
            print("Tesoura degola Lagarto!")
            win_player += 1

        elif player_choice == "Lagarto" and npc_choice == "Papel":
            print("Lagarto come Papel!")
            win_player += 1

        elif player_choice == "Papel" and npc_choice == "Spok":
            print("Papel refuta Spok!")
            win_player += 1

        elif player_choice == "Spok" and npc_choice == "Pedra":
            print("Spok vaporiza Pedra!")
            win_player += 1

        elif player_choice == "Pedra" and npc_choice == "Tesoura":
            print("E como sempre foi Pedra esmaga Tesoura!")
            win_player += 1

        # Condições de Derrota

        else:
            print("Oooohh, Você perdeu, tente novamente!")
            win_npc += 1

        # Mensagem de Vitória

        if win_player == 3:
            print("\nBazinga Sheldon é o novo campeão!")
            print(f"\nPlacar: Jogador {win_player} x {win_npc} NPC\n")
            break
        elif win_npc == 3:
            print("\nDor, perdemos para a máquina!")
            print(f"\nPlacar: Jogador {win_player} x {win_npc} NPC\n")
            break


TheBigBangJoKenPo()