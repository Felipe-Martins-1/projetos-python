import socket
import threading
from time import strftime

# 11/05/2022
class Server:
    __host = ""
    __port = 0
    __server_socket = None
    __clients = []

    def configure_connection(self, host: str, port: int) -> None:
        self.__host = host
        self.__port = port

    def start_server(self) -> None:

        # Configuração do objeto (IPV4 e Protocolo TCP)
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__server_socket.bind((self.__host, self.__port))

            # Espera conecxões e limita a quantidade
            self.__server_socket.listen(3)

            print(
                f"SERVIDOR INICIADO NO HOST '{self.__host}' E ESCUTANDO NA PORTA '{self.__port}'\n"
            )
        except Exception as ex:
            return print(f"ERRO AO INICIAR SERVIDOR: {ex}\n")

        thread_1 = threading.Thread(target=self.close_server, args=[])
        thread_1.start()

        while True:

            # Aceita novos clientes
            client, address = self.__server_socket.accept()
            self.__clients.append(client)
            time = strftime("%H:%M")
            print(f"CLIENTE CONECTADO ÀS {time}\nENDEREÇO: {address}\n")
            thread_2 = threading.Thread(
                target=self.receive_data, args=[client, address]
            )
            thread_2.start()

    # Recebe os dados do remetente
    def receive_data(self, client: socket, address: tuple) -> None:
        while True:
            try:
                data = client.recv(1000000)
                self.send_data(client=client, data=data)
            except Exception as ex:
                self.delete_client(client)
                print(
                    f"ERRO AO RECEBER MENSAGEM: {ex}\nCLIENTE DESCONECTADO!\nENDEREÇO: {address}\n"
                )
                break

    # Envia os dados para todos os destinatários
    def send_data(self, client: socket, data: bytes) -> None:

        # Broadcast
        for c in self.__clients:
            if c != client:
                try:
                    c.send(data)
                except Exception as ex:
                    self.delete_client(c)
                    print(
                        f"ERRO AO ENVIAR MENSAGEM PARA OS OUTROS CLIENTES: {ex}\nCLIENTE DESCONECTADO!\n"
                    )

    def delete_client(self, client: socket) -> None:
        self.__clients.remove(client)

    def close_server(self):
        while True:
            comand = str(
                input("Digite 'sair' para encerrar a execução do servidor\n")
            ).upper()
            if comand:
                if comand == "SAIR":
                    try:
                        self.__server_socket.close()
                        print("ENCERRADO!\n")
                        break
                    except Exception as ex:
                        print(f"ERRO: {ex}\n")
                else:
                    print("INVÁLIDO!\n")
            else:
                print("INVÁLIDO!\n")
