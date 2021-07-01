import PySimpleGUI as sg
from Tela import Tela
from CritografiaRSA import CritografiaRSA

class Principal:

    def __init__(self):
        self.loop()

    def loop(self):
        t = Tela()
        tela1, tela2 = t.telaMenu(), None
        while True:  
            janela, evento, valor = sg.read_all_windows()
            c = CritografiaRSA()
            if janela == tela1 and evento == sg.WIN_CLOSED:
                break
            elif janela == tela2 and evento == sg.WIN_CLOSED:
                break
            elif janela == tela1 and evento == "cripTela":
                tela1.hide()
                tela2 = t.telaCriptografar()
            elif janela == tela1 and evento == "descripTela":
                tela1.hide()
                tela2 = t.telaDescriptografar()
            elif janela == tela2 and evento == "Voltar":
                tela2.hide()
                tela1.un_hide()
            elif janela == tela2 and evento == "crip":  
                c.criptografar(valor["msg"], valor["chvE"], valor["chvN"])
            elif janela == tela2 and evento == "descrip":  
                c.descriptografar(valor["msgCrip"], valor["chvD"], valor["chvN"])

Principal()