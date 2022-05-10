from client import Client
from screen import Screen
from PySimpleGUI import read_all_windows, WIN_CLOSED, popup_get_file


def run_main():
    client = Client()
    screen = Screen()
    screen_1, screen_2, screen_3 = screen.login(), None, None

    while True:
        window, event, value = read_all_windows()

        # Fechar janela
        if event in [WIN_CLOSED, "exit"]:
            if window == screen_1:
                break
            elif window == screen_2:
                break
            elif window == screen_3:
                client.close_client()
                break

        # Limpar campos
        elif event == "reset":
            if window == screen_1:
                screen_1["password"].update("")
                screen_1["information"].update("")
            elif window == screen_2:
                screen_2["name"].update("")
                screen_2["position"].update("Não selecionado")
                screen_2["host"].update("Não selecionado")
                screen_2["port"].update("8000")
                screen_2["information"].update("")
            elif window == screen_3:
                screen_3["historic"].update("")
                screen_3["message"].update("")

        # Enviar dados
        elif event == "submit":
            if window == screen_1:
                password = value["password"]
                if client.login(password=password):
                    screen_1.hide()
                    screen_2 = screen.to_setup()
                else:
                    screen_1["information"].update("Senha incorreta!")

            elif window == screen_2:
                name = value["name"]
                position = value["position"]
                host = value["host"]
                port = int(value["port"])
                client.set_name(name=name)
                client.set_position(position=position)
                client.configure_connection(host=host, port=port)

                if client.start_client():
                    screen_2.hide()
                    screen_3 = screen.send_message()
                    screen_3["name"].update(client.get_name())
                    screen_3["position"].update(client.get_position())
                else:
                    screen_2["information"].update("Erro ao conectar!")

            elif window == screen_3:
                message = value["message"]
                screen_3["message"].update("")
                client.send_message(message=message)

        # Enviar arquivo
        elif event == "send_file":
            path = str(
                popup_get_file(
                    "Enviar arquivo",
                    no_window=True,
                )
            )
            client.send_message(message="/sendfile")
            client.send_file(path_2=path)

        # Setar valores
        elif window == screen_2 and event == "presets":
            screen_2["host"].update("127.0.0.1")
            screen_2["port"].update("8080")

    screen_1.close()
    if screen_2:
        screen_2.close()
    if screen_3:
        screen_3.close()


if __name__ == "__main__":
    run_main()
