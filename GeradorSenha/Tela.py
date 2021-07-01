from PySimpleGUI import PySimpleGUI as sg

class Tela:
    def __init__(self):
        sg.theme("Dark Gray")
        
    def telaPrincipal(self):
        tela = [
            [sg.Slider(range=(4, 30), default_value=0, orientation="h", size=(11.5,16), key="qtdCaracteres")],
            [sg.Checkbox("A-Z", key="letrasMaiusculas"), sg.Checkbox("a-z", key="letrasMinusculas"), sg.Checkbox("0-9", key="numeros"), sg.Checkbox("!@#$%^&*", key="simbolos"), sg.Checkbox("Tudo", key="tudo")],
            [sg.Output(size=(50, 1))],
            [sg.Button("Gerar", key="gerar")]
        ]
        return sg.Window("Gerador de Senha", layout=tela, finalize=True)