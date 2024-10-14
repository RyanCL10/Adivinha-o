import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print("Escolha a dificuldade do jogo!")
    nivel = int(input("(1)Fácil (2)Médio (3)Difícil\n"))
    numero_secreto = round(random.randrange(1, 101))
    tentativas = 0
    pontos = 1000
    if(nivel == 1):
        tentativas = 20
    elif(nivel ==2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5
    for rodada in range (1, tentativas +1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute_str = int(input("Digite um numero entre 1 e 100: \n"))
        print("Você digitou " , chute_str)
        chute = int(chute_str)
        if (chute < 0 or chute > 100):
            print("Escolha um número entre 1 e 100")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"Parabéns! Você acertou e fez {pontos} pontos!")
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = (pontos-pontos_perdidos)
    print("Fim do jogo")
    print(f"Seu Número era : {numero_secreto}")
if __name__ == '__main__':
    jogar()