from Jogo import Jogo
from time import sleep
from os import system

class Principal:

    def iniciarPrograma(self):
        system("cls") or None
        print("> Bem vindo")
        sleep(0.8)
        system("cls") or None
        print("> Bem vindo ao clássico")
        sleep(0.8)
        system("cls") or None
        print("> Bem vindo ao clássico \"Jogo da Velha\"")
        sleep(2)

        Jogo().iniciarJogo()

Principal.iniciarPrograma()