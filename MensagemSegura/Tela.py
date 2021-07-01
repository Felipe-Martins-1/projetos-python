import PySimpleGUI as sg

class Tela:

    def __init__(self):
        sg.theme("DarkTeal10")

    def telaMenu(self):
        tela = [
            [sg.Button("Criptografar", key="cripTela"), sg.Button("Descriptografar", key="descripTela")]
        ]
        return sg.Window("Menu", layout=tela, finalize=True)

    def telaCriptografar(self):
        tela = [
            [sg.Text("Mensagem")],
            [sg.Input(key="msg", size=(40, 5))],
            [sg.Text("Chave E")],
            [sg.Input(key="chvE", size=(8, 0))],
            [sg.Text("Chave N")],
            [sg.Input(key="chvN", size=(8, 0))],
            [sg.Button("Criptografar", key="crip"), sg.Button("Voltar")],
            [sg.Text("Mensagem criptografada")],
            [sg.Output(size=(40, 10))]
        ]
        return sg.Window("Criptografar mensagem", layout=tela, finalize=True)

    def telaDescriptografar(self):
        tela = [
            [sg.Text("Mensagem criptografada")],
            [sg.Input(key="msgCrip", size=(40, 5))],
            [sg.Text("Chave D")],
            [sg.Input(key="chvD", size=(8, 0))],
            [sg.Text("Chave N")],
            [sg.Input(key="chvN", size=(8, 0))],
            [sg.Button("Descriptografar", key="descrip"), sg.Button("Voltar")],
            [sg.Text("Mensagem descriptografada")],
            [sg.Output(size=(40, 10))]
        ]
        return sg.Window("Descriptografar mensagem", layout=tela, finalize=True)