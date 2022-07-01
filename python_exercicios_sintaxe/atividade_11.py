#Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo 
# pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. 
# Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo. 
# Saída: Apresente a duração do jogo conforme exemplo abaixo



#função para verificar a duração do jogo
def duracao(horaInicial, horaFinal):
    #Na lógica precisamos determinar o tempo de jogo, lembrando que o dia tem 24 horas.
    if horaInicial > horaFinal:
        return f'O jogo durou {(24 - (horaInicial - horaFinal))} hora(s)'
    elif horaFinal > horaInicial:
        return f'O jogo durou {(horaFinal - horaInicial)} horas(s)'
    return print(f'O jogo durou 24 horas(s)')


#recebendo os valores de inicio e fim jogo
horaInicial = int(input('Informe a hora inicial do jogo? '));
horaFinal = int(input('Informe a hora final do jogo? '));

#imprimir o resultado chamando a função duracao
print(duracao(horaInicial, horaFinal))
