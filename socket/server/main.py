from server import Server
from getpass4 import getpass


def run_main():
    server = Server()
    while True:
        while True:
            password = getpass(prompt="Senha: ", char="*")
            if password:
                if password == "server1234":
                    break
                else:
                    print("SENHA INVÁLIDO!\n")
            else:
                print("INVÁLIDO!\n")
        presets = str(
            input(
                "Usar valores predefinidos?\nHost: localhost\nPorta: 8080\nSim ou não: "
            )
        ).upper()
        if presets == "SIM":
            host = "localhost"
            port = 8080
            break
        elif presets in ["NAO", "NÃO"]:
            host = str(input("Host: "))
            port = int(input("Porta: "))
            break
        else:
            print("\nINVÁLIDO!\n")
    server.configure_connection(host=host, port=port)
    server.start_server()


if __name__ == "__main__":
    run_main()
