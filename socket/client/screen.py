from tkinter import CENTER
from PySimpleGUI import (
    theme,
    Text,
    Input,
    Combo,
    Slider,
    Button,
    Output,
    Multiline,
    Window,
)


class Screen:
    def __init__(self) -> None:
        theme("Dark")

    def login(self) -> Window:
        screen = [
            [Text("Senha")],
            [Input(key="password", password_char="*", focus=True)],
            [Text("", key="information")],
            [Button("Entrar", key="submit", size=(11, 1))],
            [
                Button("Limpar", key="reset"),
                Button("Sair", key="exit"),
            ],
        ]
        return Window(
            "Login",
            layout=screen,
            element_justification=CENTER,
            finalize=True,
            font=("Roboto", 11),
        )

    def to_setup(self) -> Window:
        screen = [
            [
                Text("Nome"),
                Input(key="name", size=(15, 10), focus=True),
                Text(""),
                Text("Posição"),
                Combo(
                    ["Não selecionado", "Secretaria", "Inspetor"],
                    key="position",
                    default_value="Não selecionado",
                ),
            ],
            [
                Text("Host"),
                Combo(
                    ["Selecionar", "127.0.0.1"],
                    key="host",
                    default_value="Selecionar",
                ),
                Text(""),
                Text("Porta"),
                Slider(
                    range=(8000, 8200),
                    default_value=0,
                    orientation="h",
                    size=(12, 20),
                    key="port",
                ),
            ],
            [Text("", key="information")],
            [Button("Conectar", key="submit", size=(24, 1))],
            [
                Button("Predefinições", key="presets"),
                Button("Limpar", key="reset"),
                Button("Sair", key="exit"),
            ],
        ]
        return Window(
            "Configurações",
            layout=screen,
            element_justification=CENTER,
            finalize=True,
            font=("Roboto", 11),
        )

    def send_message(self) -> Window:
        screen = [
            [Text("Nome", key="name"), Text("Posição", key="position")],
            [Text("Histórico")],
            [Output(key="historic", size=(55, 20), metadata=True)],
            [Text("Mesagem")],
            [
                Multiline(
                    key="message",
                    size=(55, 5),
                    focus=True,
                )
            ],
            [Button("Enviar mensagem", key="submit", size=(24, 1))],
            [
                Button("Enviar arquivo", key="send_file"),
                Button("Limpar", key="reset"),
                Button("Sair", key="exit"),
            ],
        ]
        return Window(
            "Chat",
            layout=screen,
            element_justification=CENTER,
            finalize=True,
            font=("Roboto", 11),
        )
