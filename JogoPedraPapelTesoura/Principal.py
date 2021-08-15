from os import system
from Jogo import Jogo

system("cls") or None
nome = str(input("Seu nome: "))

while True:
    system("cls") or None
    resposta = str(input("pedra, papel ou tesoura? "))
    if resposta == "0":
        break
    else:
        jogo = Jogo(nome, resposta)