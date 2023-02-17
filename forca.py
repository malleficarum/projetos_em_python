import random


def jogar():
    header()

    carregar_lista_palavras()
    palavra_secreta = carregar_lista_palavras()
    letras_acertadas = ['_' for letra in palavra_secreta]  # lista para guardar as posições das letras acertadas

    # como o jogador ainda não enforcou e nem acertou a palavra, os valores começarão como falsos
    print('{}'.format(len(palavra_secreta)))
    print(letras_acertadas, '\n')

    enforcou = False
    acertou = False
    erros = 0
    # enquanto não enforcou e não acertou (not false/true), o laço continuará
    while not enforcou and not acertou:

        chute = pede_chute()
        # print(palavra_secreta.find(chute)) devolve a posição, na palavra secreta, da letra chutada. lembre-se: a
        # contagem de posição se inicia em 0 e não em 1 (ex.: a letra A ocupa a posição 2 na palavra 'dracula). ele
        # não será utilizado aqui por esse motivo!
        if chute in palavra_secreta:
            indice_de_acertos(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print('Você errou! Faltam {} tentativa(s).'.format(6 - erros))

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        continuidade(letras_acertadas)

    if acertou:
        mensagem_ganhador()
    elif enforcou:
        mensagem_perdedor(palavra_secreta)


def header():
    print("**********************************")
    print("Bem vindo ao jogo de Forca!")
    print("**********************************", end="\n\n")


def carregar_lista_palavras():
    lista = open('lista.txt', 'r')  # abrimos uma lista em .txt para escolha aleatoria das palavras.
    palavras = []  # tupla que seja inserida as palavras contidas no arquivo .txt.
    for linha in lista:
        linha = linha.strip()  # retirada do /n após cada palavra.
        palavras.append(linha)  # anexando cada linha na tupla supramencionada.
    lista.close()  # fechamento da leitura do arquivo .txt

    numero = random.randrange(0, len(palavras))  # criaremos um numero aleatorio para usar como indice para escolha da
    # palavra. ele utiliza o proprio indice da lista, que vai de 0 ate a ultima linha.
    palavra_secreta = palavras[numero].upper()  # criaremos a variavel 'palavra-secreta', deixando em letra maiuscula

    return palavra_secreta


def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute


def indice_de_acertos(palavra_s, chute_, letras_a):
    index = 0  # posição = index
    for letra in palavra_s:
        if chute_ == letra:
            letras_a[index] = letra
        index += 1


def continuidade(letras_a):
    print(letras_a)
    print('Jogando...\n')


def mensagem_ganhador():
    print('Ufa! Você sobreviveu... dessa vez.')
    print('       ___________      ')
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_s):
    print('Você enforcooou.')
    print('A palavra secreta era "{}"'.format(palavra_s))
    print('  _____')
    print(' /     \ ')
    print('| () () |')
    print(' \  ^  /')
    print('  |||||')
    print('  |||||')


if __name__ == '__main__':
    jogar()
