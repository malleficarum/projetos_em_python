import forca
import adivinhação


# importação dos módulos forca & adivinhação como bibliotecas. para evitar que o python execute o arquivo assim que
# chamá-lo (no import), estabelecemos uma verificação nos outros módulos de que o programa está sendo executado por
# si só. igualaremos então a variável __name__ a variável __main__, criando uma condição.

def escolhe_jogo():
    header()

    print('[ 1 ] Forca \n[ 2 ] Adivinhação \n')
    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        jogar_forca()

    elif jogo == 2:
        jogar_adivinhacao()


def header():
    print("**********************************")
    print("Bem vindo ao módulo de jogos!")
    print("**********************************", end="\n\n")


def jogar_forca():
    print('Jogando { Forca! }')
    forca.jogar()  # função criada para chamar a execução do arquivo forca


def jogar_adivinhacao():
    print('Jogando { Adivinhação! }')
    adivinhação.jogar()  # função criada para chamar a execução do arquivo adivinhação


if __name__ == '__main__':
    escolhe_jogo()
