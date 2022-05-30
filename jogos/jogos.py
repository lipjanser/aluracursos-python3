import adivinhacao
import forca

def escolher_jogo():
    print("***********************************")
    print("********Escolha o seu jogo*********")
    print("***********************************")

    try:
        jogo = int(input("Forca(1)---Adivinhação(2): "))
        if jogo == 1:
            print("Abrindo o jogo Forca!")
            forca.jogar()
        elif jogo == 2:
            print("Abrindo o jogo Adivinhação!")
            adivinhacao.jogar()
        else:
            print("Entrada inválida!")
    except:
        print("Entrada inválida!")

if (__name__ == "__main__"):
    escolher_jogo()