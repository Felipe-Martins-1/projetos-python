from PySimpleGUI import read_all_windows, WIN_CLOSED
from Tela import Tela
from GeradorSenha import GeradorSenha

class Principal:

    def iniciarPrograma(self):
        t = Tela()
        tela = t.telaPrincipal()
        while True:
            janela, evento, valor = read_all_windows()
            if janela == tela and evento == WIN_CLOSED:
                break
            elif janela == tela and evento == "gerar":
                GeradorSenha(int(valor["qtdCaracteres"]), valor["letrasMaiusculas"], valor["letrasMinusculas"], valor["numeros"], valor["simbolos"], valor["tudo"])

Principal().iniciarPrograma()