from PySimpleGUI import PySimpleGUI as sg
from Tela import Tela
from GeradorSenha import GeradorSenha

class Principal:
    def __init__(self):
        self.loop()

    def loop(self):
        t = Tela()
        tela = t.telaPrincipal()
        while True:
            janela, evento, valor = sg.read_all_windows()
            if janela == tela and evento == sg.WIN_CLOSED:
                break
            elif janela == tela and evento == "gerar":
                GeradorSenha(int(valor["qtdCaracteres"]), valor["letrasMaiusculas"], valor["letrasMinusculas"], valor["numeros"], valor["simbolos"], valor["tudo"])

Principal()