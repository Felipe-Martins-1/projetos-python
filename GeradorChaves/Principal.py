from PySimpleGUI import read_all_windows, WIN_CLOSED
from Tela import Tela
from GeradorChaves import GeradorChaves

class Principal:

    def iniciarPrograma(self):
        tela = Tela().telaPrincipal()
        while True:
            janela, evento = read_all_windows()
            if janela == tela and evento == WIN_CLOSED:
                break
            elif janela == tela and evento == "gerar":
                GeradorChaves()

Principal().iniciarPrograma()