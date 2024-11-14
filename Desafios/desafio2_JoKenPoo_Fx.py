""" Trilha de Python  - for_code [ ] - Semana Dois -  Márcio Melchiades Nascimento """

# Questão 1: Fazer um pedra, papel, tesoura, lagarto e Spok, Utilizando Funções.

# Importação da biblioteca random, sys e time

from random import choice
from time import sleep
from sys import exit

# Definição da função


def menu() -> str:
    """
    Função que exibe o menu de opções do jogo.

    params:: str

    return:: str
    """
    
    game_state = "menu"

    # Definição do estado do jogo
    print("\nBem-vindo ao JoKenPo!")

    print("\n1 - Jogar")
    print("2 - Créditos")
    print("3 - Regras")
    print("4 - Sair do JoKenPo\n")
            
    resposta = input("Escolha uma opção: ")
            
    if  resposta == "1":
        game_state = "play"
            
    elif resposta == "2":
        game_state = "credits"
            
    elif resposta == "3":
        game_state = "rules"
            
    elif resposta == "4":
        game_state = "exit"

    return game_state



def TheBigBangJoKenPo():
    """
    Função que executa o jogo JoKenPo com as regras de Pedra, Papel, Tesoura, Lagarto e Spok.

    params:: None   

    return:: None
    """
    
    # Definição das opções possíveis

    escolhas = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spok"]

    # Definição da quantidade de rodadas

    win_player = 0
    win_npc = 0
    empate = 0

    status = menu()

    # Loop para verficar Status do Jogo
    while True:

        match status:
            case "play":
                
                # Loop para o jogo Rodar
                while True:
                    
                    # Escolha do jogador e do NPC

                    player_choice = input("\nEscolha entre pedra, papel, tesoura, lagarto e Spok: ")
                    player_choice = player_choice.capitalize()
                    npc_choice = choice(escolhas)
                    
                    print() # Pular linha
                    
                    # Mensagem de JO KEN PO
                    sleep(0.5)
                    for i in escolhas:
                        sleep(0.3)
                        print(i)
                    sleep(0.5)
                    
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
                        status = menu()
                        break
                    elif win_npc == 3:
                        print("\nDor, perdemos para a máquina!")
                        print(f"\nPlacar: Jogador {win_player} x {win_npc} NPC\n")
                        status = menu()
                        break


            case "credits":
                print("\nDesenvolvido por: Márcio Melchiades Nascimento")
                print("Email: marciomelchiades.20221@poli.ufrj.br")
                print("GitHub: mahttps://github.com/marciomn01")
                print("LinkedIn: https://www.linkedin.com/in/marciomelchiadesnascimento/?originalSubdomain=br\n")
                
                # Back to menu

                print("Pressione Enter para voltar ao menu...")
                
                aux = input("")
                
                if aux == "":
                    status = "menu"

            case "rules":
                print("\nRegras do JoKenPo:")
                print("\n1 - Pedra esmaga Tesoura")
                print("2 - Tesoura corta Papel")
                print("3 - Papel cobre Pedra")
                print("4 - Pedra esmaga Lagarto")
                print("5 - Lagarto envenena Spok")
                print("6 - Spok amassa Tesoura")
                print("7 - Tesoura degola Lagarto")
                print("8 - Lagarto come Papel")
                print("9 - Papel refuta Spok")
                print("10 - Spok vaporiza Pedra")
                print("11 - E como sempre foi Pedra esmaga Tesoura\n")
                
                # Back to menu

                print("Pressione Enter para voltar ao menu...")
                
                aux = input("")
                
                if aux == "":
                    status = "menu"
            
            case "exit":
                print("\nObrigado por jogar o JoKenPo! Até a próxima!\n")
                exit()

            case "menu":
                status = menu()

TheBigBangJoKenPo()
