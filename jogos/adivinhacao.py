import random as rd

def jogar():
    print("***********************************")
    print("*Bem vindo ao jogo de Adivinhação!*")
    print("***********************************")

    pontuacao = 1000

    while 1==1:
        print("Selecione a dificuldade!")
        dificuldade = int(input("Fácil(1)---Médio(2)---Difícil(3):"))

        if dificuldade == 1:
            total_tentativas = 20
        elif dificuldade == 2:
            total_tentativas = 10
        elif dificuldade == 3:
            total_tentativas = 5
        else:
            print("Entrada inválida!!")

        if dificuldade >=1 and dificuldade <= 3:
            break

    numero_secreto = rd.randint(0,100)
    print("{} pontos!".format(pontuacao))

    for rodada in range(1,total_tentativas + 1):
        
        try:
            chute = int(input("(Tentativa {} / {}) Digite seu numero (0 até 100): ".format(rodada,total_tentativas)))
        except:
            print("Entrada inválida!!")
            continue

        if chute < 0 or chute > 100:
            print("Digite um número de 0 a 100.")
            continue
        
        if numero_secreto == chute:
            print("Boa jogada! Você VENCEU!!!!!!")
            print("Pontuação final: {}".format(pontuacao))
            break
        else:
            if numero_secreto < chute:
                print("Você chutou para Cima." )
            else:
                print("Você chutou para Baixo." )
                
            pontuacao -= round((abs(numero_secreto - chute)/3))
            print("{} pontos!".format(pontuacao))


        if rodada == total_tentativas:
            print("Você perdeu. Game Over!!")
            print("O número secreto era {}. Você fez {} pontos!!".format(numero_secreto, pontuacao))
            break;

if (__name__ == "__main__"):
    jogar()