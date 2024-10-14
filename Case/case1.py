'''  Processo Seletivo 2024.2 - for_code [ ] - Case 1: Ciclos do Sono Ideal'''

# Função principal

def calcular_horarios_de_sono(hora, minutos, ciclo):
    # Lista para guardar informações
    lista_horarios = []

    # Condição para o while continuar e parar.
    n = 0

    while n != 6:
        minutoNovo = minutos + ciclo * (n + 1)
        minutoFinal = minutoNovo % 60
        restominuto = minutoNovo // 60
        horaNovo = hora + restominuto
        horaFinal = horaNovo % 24
        lista_horarios.append(f"{horaFinal:02}:{minutoFinal:02}")
        
        n += 1

    return lista_horarios

# Variaveis de uso da função
hora = int(input("\nDigite a hora que você irá dormir: "))
minutos = int(input("\nDigite o minuto que você irá dormir: "))
ciclo = int(input("\nDigite o ciclo em minutos que você irá dormir: ")) # Caso o ciclo seja variável, basta mudar o valor aqui.


horarios = calcular_horarios_de_sono(hora, minutos, ciclo)
lista_ordem = ["Primeiro", "Segundo", "Tereiro", "Quarto", "Quinto", "Sexto"]

# Apenas para dar Título
print("\nCiclos do Sono Ideal:\n")

# Imprimir os horários
for ordem, horario in zip(lista_ordem, horarios):
    print(f"• {ordem} ciclo: {horario}\n")