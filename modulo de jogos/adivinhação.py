import random # importando a biblioteca random, para randomização do numero secreto.

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("**********************************", end="\n\n")

    numero_secreto = round(random.randrange(0, 101)) # gera um número entre 0 e 100 aleatoriamente.
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade você deseja?') # diálogo para escolher o nivel de dificuldade.
    print('[ 1 ] Fácil \n[ 2 ] Médio \n[ 3 ] Difícil')
    nivel = int(input('Escolha: '))

    if (nivel == 1): # estabelecimento do numero máx. de tentativas
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1): # laço de repetição principal, onde há o incremento do numero de
        # rodadas.
        print("Rodada {} de {}.".format(rodada, total_de_tentativas))

        chute = input("Digite um número de 1 a 100: ")
        print("Você digitou: ", chute)
        chute_convert = int(chute) # função de conversão da variavel chute, anteriormente uma string, para int. assim,
        # a condição da condicional if se torna verdadeira, uma vez estar comparando dois valores ints.

        if (chute_convert < 0 or chute_convert > 100): # aviso para caso o jogador digite um numero menor que zero ou
            # maior que 100.
            print('Você deve digitar um número entre 1 a 100!')
            continue # o numero digitado erroneamente contará como uma rodada.

        chute_certo = chute_convert == numero_secreto # simplificação da condição de igualdade dos valores das variaveis.
        chute_maior = chute_convert > numero_secreto # simplificação da condição de diferença dos valores das variaveis.
        chute_menor = chute_convert < numero_secreto # simplificação da condição de diferença dos valores das variaveis.

        if (chute_certo):
            print("\nVocê acertou! Pontos ganhos: {}\n".format(pontos))
            break # fim do jogo no caso de acerto.

        else:
            if (chute_maior):
                print('Seu chute foi maior que o número secreto!\n')
            elif (chute_menor):
                print('Seu chute foi menor que o número secreto!\n')
            pontos_perdidos = abs(numero_secreto - chute_convert) # pontos perdidos na rodada
            pontos = pontos - pontos_perdidos # debitando os pontos perdidos da pontuação atual

        if(rodada == total_de_tentativas):
            print('Seu número secreto era {} e você fez {} pontos.'.format(numero_secreto, pontos))

    print("Fim de jogo.") # fini.

if(__name__ == '__main__'): # permite que o código seja executado como um script quando chamado, e não importado como
    # um módulo
    jogar()