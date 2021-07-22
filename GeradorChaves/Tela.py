from tkinter.constants import CENTER
from PySimpleGUI import Output, Button, Window, theme

class Tela:
    def __init__(self):
        theme("DarkTeal10")
        
    def telaPrincipal(self):
        tela = [
            [Output(size=(15, 4))],
            [Button("Gerar", key="gerar")]
        ]
        return Window("Gerador de Chaves", layout=tela, finalize=True, size=(250, 120), element_justification=CENTER)