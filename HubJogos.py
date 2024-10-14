import adivinhacao
import forca
print("*********************************")
print("***Bem vindo ao jogo de Forca!***")
print("*********************************")
print("Escolha o jogo!")
jogo= int(input("(1)Forca (2)Adivinhacao\n"))
if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    adivinhacao.jogar()