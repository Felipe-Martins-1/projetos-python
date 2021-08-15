from random import choice
from time import sleep
from os import system

class Jogo:

    def __init__(self):
        self.posicoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.posicoesSobrando = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.pontuacaoJogador1 = 0
        self.pontuacaoJogador2 = 0

    def resertarValores(self):
        self.posicoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.posicoesSobrando = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # É INFORMADO A QUANTIDADE DE JOGADORES E QUANDO O JOGO CONTINUA OU TERMINA
    def iniciarJogo(self):
        system("cls") or None
        while True:    
            print("> Apenas 1 jogador ou 2 jogadores?")
            qtdJogador = int(input(": "))
            system("cls") or None
            if qtdJogador == 1:
                print("Qual o nome do jogador 1?")
                nomeJogador1 = str(input(": "))
                system("cls") or None
                nomeJogador2 = "Bot"
                system("cls") or None
                self.determinarValores(nomeJogador1, nomeJogador2)
                while True:
                    if self.iniciarOutraPartida() == True:
                        system("cls") or None
                        self.resertarValores()
                        self.determinarValores(nomeJogador1, nomeJogador2)
                    else:
                        system("cls") or None
                        self.mostrarPlacar(nomeJogador1, nomeJogador2)
                        break
                break
            elif qtdJogador == 2:
                print("> Qual o nome do jogador 1?")
                nomeJogador1 = str(input(": "))
                system("cls") or None
                print("> Qual o nome do jogador 2?")
                nomeJogador2 = str(input(": "))
                system("cls") or None
                self.determinarValores(nomeJogador1, nomeJogador2)
                while True:
                    if self.iniciarOutraPartida() == True:
                        system("cls") or None
                        self.resertarValores()
                        self.determinarValores(nomeJogador1, nomeJogador2)
                    else:
                        system("cls") or None
                        self.mostrarPlacar(nomeJogador1, nomeJogador2)
                        break
                break
            else:
                system("cls") or None
                print("> Quantidade inválida!")
                sleep(2)
                system("cls") or None
    
    def iniciarOutraPartida(self):
        system("cls") or None
        while True:
            print("> Continuar? [s/n]")
            comando = str(input(": "))
            if comando == "s":
                status = True
                break
            elif comando == "n":
                status = False
                break
            else:
                system("cls") or None
                print("> Comando inválido!")
                sleep(2)
                system("cls") or None
        return status        

    # DETERMINA OS VALORES PARA CADA JOGADOR DE MODO ALEATÓRIO 
    def determinarValores(self, nomeJogador1, nomeJogador2):
        valores = ["X", "O"]
        valorJogador1 = choice(valores)
        if valorJogador1 == "X":
            valorJogador2 = "O"
            print(f"> {nomeJogador1}: {valorJogador1}")
            print(f"> {nomeJogador2}: {valorJogador2}")
        else:
            valorJogador2 = "X"
            print(f"> {nomeJogador1}: {valorJogador1}")
            print(f"> {nomeJogador2}: {valorJogador2}")
        self.determinarPrimeiroJogador(nomeJogador1, nomeJogador2, valorJogador1, valorJogador2)
    
    # DETERMINA QUAL JOGADOR COMEÇA A JOGAR DE MODO ALEATÓRIO
    def determinarPrimeiroJogador(self, nomeJogador1, nomeJogador2, valorJogador1, valorJogador2):
        nomes = [nomeJogador1, nomeJogador2]
        nomeVariavel = choice(nomes)
        print(f"> {nomeVariavel} começa!")
        sleep(3)
        system("cls") or None
        self.jogar(nomeVariavel, nomeJogador1, nomeJogador2, valorJogador1, valorJogador2)

    # TROCA O JOGADOR APÓS A CADA JOGADA E MOSTRA O RESULTADO DA PARTIDA
    def jogar(self, nomeVariavel, nomeJogador1, nomeJogador2, valorJogador1, valorJogador2):
        for i in range(9):
            if self.validarVitoria() == False:
                if i > 0:
                    if nomeVariavel == nomeJogador1:
                        nomeVariavel = nomeJogador2
                        self.setarValorPosicao(nomeJogador2, valorJogador2)
                    else:
                        nomeVariavel = nomeJogador1
                        self.setarValorPosicao(nomeJogador1, valorJogador1)
                else:
                    if nomeVariavel == nomeJogador1:
                        self.setarValorPosicao(nomeJogador1, valorJogador1)
                    else:
                        self.setarValorPosicao(nomeJogador2, valorJogador2)
            else:
                print(f"{nomeVariavel} ganhou!")
                sleep(2)
                system("cls") or None
                self.setarPontuacaoPlacar(nomeVariavel, nomeJogador1)
                self.mostrarPlacar(nomeJogador1, nomeJogador2)
                system("cls") or None
                break
        else:
            print("Empate!")
            sleep(2)
            system("cls") or None
            self.mostrarPlacar(nomeJogador1, nomeJogador2)
    
    # SOMATÓRIA DE VITÓRIAS
    def setarPontuacaoPlacar(self, nomeVariavel, nomeJogador1):
        if nomeVariavel == nomeJogador1:
            self.pontuacaoJogador1 += 1
        else:
            self.pontuacaoJogador2 += 1

    def mostrarPlacar(self, nomeJogador1, nomeJogador2):
        print(f"> Placar = {nomeJogador1}: {self.pontuacaoJogador1}\n           {nomeJogador2}: {self.pontuacaoJogador2}")
        sleep(3) 

    # VERIFICA E VALÍDA A VITÓRIA
    def validarVitoria(self):
        status = False

        # POSSIBILIDADES DE VITÓRIA COM O VALOR "X"
        if self.posicoes[0] == "X" and self.posicoes[1] == "X" and self.posicoes[2] == "X":
            status = True
        elif self.posicoes[3] == "X" and self.posicoes[4] == "X" and self.posicoes[5] == "X":
            status = True
        elif self.posicoes[6] == "X" and self.posicoes[7] == "X" and self.posicoes[8] == "X":
            status = True
        elif self.posicoes[0] == "X" and self.posicoes[3] == "X" and self.posicoes[6] == "X":
            status = True
        elif self.posicoes[1] == "X" and self.posicoes[4] == "X" and self.posicoes[7] == "X":
            status = True
        elif self.posicoes[2] == "X" and self.posicoes[5] == "X" and self.posicoes[8] == "X":
            status = True
        elif self.posicoes[0] == "X" and self.posicoes[4] == "X" and self.posicoes[8] == "X":
            status = True
        elif self.posicoes[2] == "X" and self.posicoes[4] == "X" and self.posicoes[6] == "X":
            status = True
        
        # POSSIBILIDADES DE VITÓRIA COM O VALOR "O"
        if self.posicoes[0] == "O" and self.posicoes[1] == "O" and self.posicoes[2] == "O":
            status = True
        elif self.posicoes[3] == "O" and self.posicoes[4] == "O" and self.posicoes[5] == "O":
            status = True
        elif self.posicoes[6] == "O" and self.posicoes[7] == "O" and self.posicoes[8] == "O":
            status = True
        elif self.posicoes[0] == "O" and self.posicoes[3] == "O" and self.posicoes[6] == "O":
            status = True
        elif self.posicoes[1] == "O" and self.posicoes[4] == "O" and self.posicoes[7] == "O":
            status = True
        elif self.posicoes[2] == "O" and self.posicoes[5] == "O" and self.posicoes[8] == "O":
            status = True
        elif self.posicoes[0] == "O" and self.posicoes[4] == "O" and self.posicoes[8] == "O":
            status = True
        elif self.posicoes[2] == "O" and self.posicoes[4] == "O" and self.posicoes[6] == "O":
            status = True
        return status

    # É INFORMADO QUAL POSIÇÃO E A MESMA É VERIFICA E SETADA COM O VALOR CORRESPONDENTE 
    def setarValorPosicao(self, nomeVariavel, valor):
        while True:
            if nomeVariavel != "Bot":
                print(f"> {nomeVariavel}\n> {valor}")
                self.mostrarTabuleiro()
                print("Qual a posição?")
                posicao = int(input(": "))
                system("cls") or None
            
            # BOT
            else:
                system("cls") or None
                print(f"> {nomeVariavel}\n> {valor}")
                sleep(0.5)
                system("cls") or None
                print(f"> {nomeVariavel}.\n> {valor}")
                sleep(0.5)
                system("cls") or None
                print(f"> {nomeVariavel}..\n> {valor}")
                sleep(0.5)
                system("cls") or None
                print(f"> {nomeVariavel}...\n> {valor}")
                sleep(0.5)
                system("cls") or None
                posicao = int(choice(self.posicoesSobrando))
            
            if self.verificarPosicao(posicao) == False:
                if posicao == 1:
                    self.posicoes[0] = valor
                    self.posicoesSobrando.remove("1")
                    break
                elif posicao == 2:
                    self.posicoes[1] = valor
                    self.posicoesSobrando.remove("2")
                    break
                elif posicao == 3:
                    self.posicoes[2] = valor
                    self.posicoesSobrando.remove("3")
                    break
                elif posicao == 4:
                    self.posicoes[3] = valor
                    self.posicoesSobrando.remove("4")
                    break
                elif posicao == 5:
                    self.posicoes[4] = valor
                    self.posicoesSobrando.remove("5")
                    break
                elif posicao == 6:
                    self.posicoes[5] = valor
                    self.posicoesSobrando.remove("6")
                    break
                elif posicao == 7:
                    self.posicoes[6] = valor
                    self.posicoesSobrando.remove("7")
                    break
                elif posicao == 8:
                    self.posicoes[7] = valor
                    self.posicoesSobrando.remove("8")
                    break
                elif posicao == 9:
                    self.posicoes[8] = valor
                    self.posicoesSobrando.remove("9")
                    break
                else:
                    print("> Posição inválida!")
                    sleep(2)
                    system("cls") or None
            else:
                system("cls") or None
                print(f"> Posição ocupada!")
                sleep(2)
                system("cls") or None

    # VERIFICA E VALÍDA A POSIÇÃO
    def verificarPosicao(self, posicao):
        status = False
        if posicao == 1 and self.posicoes[0] in ["X", "O"]:
            status = True
        elif posicao == 2 and self.posicoes[1] in ["X", "O"]:
            status = True
        elif posicao == 3 and self.posicoes[2] in ["X", "O"]:
            status = True
        elif posicao == 4 and self.posicoes[3] in ["X", "O"]:
            status = True
        elif posicao == 5 and self.posicoes[4] in ["X", "O"]:
            status = True
        elif posicao == 6 and self.posicoes[5] in ["X", "O"]:
            status = True
        elif posicao == 7 and self.posicoes[6] in ["X", "O"]:
            status = True
        elif posicao == 8 and self.posicoes[7] in ["X", "O"]:
            status = True
        elif posicao == 9 and self.posicoes[8] in ["X", "O"]:
            status = True
        return status

    def mostrarTabuleiro(self):
        print(f"\t\t {self.posicoes[0]} | {self.posicoes[1]} | {self.posicoes[2]}\n\t\t---|---|---\n\t\t {self.posicoes[3]} | {self.posicoes[4]} | {self.posicoes[5]}\n\t\t---|---|---\n\t\t {self.posicoes[6]} | {self.posicoes[7]} | {self.posicoes[8]}")