import random as rd

def jogar():
    palavras = abrir_arquivo_palavras()
    palavra_secreta = sortear_palavra_secreta(palavras)
    arr_letras_ocultas = ["_" for letra in palavra_secreta]
    total_tentativas = 7
    enforcou = False
    acertou = False
    erros = 0

    imprimir_mensagem_abertura()
    while True:
        imprimir_tentativas_restantes(arr_letras_ocultas,total_tentativas - erros)
        chute = pedir_chute()
        if chute in palavra_secreta:
            marcar_chute_correto(chute, arr_letras_ocultas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        if erros == total_tentativas:
            break
        if "_" not in arr_letras_ocultas:
            break
    
    fim_de_jogo(arr_letras_ocultas,palavra_secreta) 

def abrir_arquivo_palavras():
    with open("palavras.txt","r") as arquivo:  
        palavras = arquivo.readlines()
    return palavras

def sortear_palavra_secreta(palavras):
    while True:
        indice = rd.randrange(0,len(palavras))
        # A maior palavra da língua portuguesa tem 46 letras
        if len(palavras[indice].strip()) <= 46:
            break

    return palavras[indice].strip().upper()

def imprimir_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def imprimir_tentativas_restantes(arr_letras_ocultas, tentativas_restantes):
    print(arr_letras_ocultas)
    print("Restam {} tentativas.".format(tentativas_restantes))
    
def pedir_chute():
    while True:
        chute = input("Informe uma letra: ").upper().strip()[0]
        if not chute.isalpha:
            continue
        return chute

def marcar_chute_correto(chute, arr_letras_ocultas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if letra.upper() == chute:
            arr_letras_ocultas[index] = chute
            imprimir_letra_encontrada(arr_letras_ocultas, chute, index)
        index += 1    

def imprimir_letra_encontrada(arr_letras_ocultas, chute, index):
    print("Encontrei a letra {} na posição {}".format(chute,index + 1))
    if arr_letras_ocultas.count("_") != 0:
        print("Faltam {} letras!".format(arr_letras_ocultas.count("_")))

def fim_de_jogo(arr_letras_ocultas, palavra_secreta):
    if "_" not in arr_letras_ocultas:
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    elif erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    elif erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    elif erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    elif erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    else:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(palavra_secreta):
    print("A palavra secreta é {}. Parabéns, você ganhou!".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"):
    jogar()