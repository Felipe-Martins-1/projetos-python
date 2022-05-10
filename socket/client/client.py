import threading
import socket
from time import strftime
from os import path, mkdir

# 11/05/2022
class Client:
    __name = ""
    __position = ""
    __host = ""
    __port = 0
    __client_socket = None

    def __init__(self) -> None:
        pass

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if name == "":
            name = "Sem nome"
        self.__name = name

    def get_position(self) -> str:
        return self.__position

    def set_position(self, position: str) -> None:
        self.__position = position

    def __shorten_name(self, file_name: str) -> str:
        file_name = file_name[::-1]
        name = ""
        for character in file_name:
            if character not in ["\\", "/"]:
                name += character
            else:
                break
        return name[::-1]

    def login(self, password: str) -> bool:
        status = False
        if password:
            if password == "client1234":
                status = True
        return status

    def configure_connection(self, host: str, port: int) -> None:
        self.__host = host
        self.__port = port

    def start_client(self) -> bool:
        status = True

        # IPV4 e Protocolo TCP
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__client_socket.connect((self.__host, self.__port))
            print("CONECTADO!\n")
        except Exception as ex:
            print(f"ERRO AO CONECTAR: {ex}\n")
            status = False

        # Inicia thread
        thread = threading.Thread(target=self.__receive_message, args=[])
        thread.start()

        return status

    def __receive_message(self) -> None:
        while True:
            try:
                # recv determina a quantidade máxima de bytes aceitos
                data = eval(self.__client_socket.recv(1024).decode("utf-8").rstrip())
                name = data["name"]
                position = data["position"]
                message = data["message"]
                time = strftime("%H:%M")

                if message == "/sendfile":
                    data = eval(
                        self.__client_socket.recv(1024).decode("utf-8").rstrip()
                    )
                    self.__receive_file(name=name, data=data)
                else:
                    print(f"{name} ({position}) as {time}\n{message}\n")

            except Exception as ex:
                print(f"ERRO AO RECEBER A MENSAGEM: {ex}\nVOCÊ FOI DESCONECTADO!\n")
                self.close_client()
                break

    def __receive_file(self, name: str, data: bytes) -> None:
        try:
            file_extension = data["file_extension"]
            file_size = data["file_size"]
            user_directory = path.expanduser("~\\")
            time = strftime("%d%m%Y%H%M%S")

            # Verifica se pasta existe
            if path.isdir(user_directory + "Desktop\\Arquivos recebidos") == False:
                mkdir(user_directory + "Desktop\\Arquivos recebidos")
                print("DIRETÓRIO 'Arquivos recebidos' CRIADO NA ÁREA DE TRABALHO!\n")

            file_path = path.join(
                user_directory
                + "Desktop\\Arquivos recebidos\\"
                + f"{time}"
                + file_extension
            )

            with open(file_path, "wb") as file:
                while file_size != str(path.getsize(file_path)):
                    data = self.__client_socket.recv(1000000)
                    file.write(data)
                    if int(file_size) < 10000:
                        break

            message = "Recebi seu arquivo com sucesso!"
            user_data = str(
                {
                    "name": f"{self.__name}",
                    "position": f"{self.__position}",
                    "message": f"{message}",
                }
            )
            self.__client_socket.send(user_data.encode("utf-8"))
            print(f"VOCÊ RECEBEU UM ARQUIVO: '{time + file_extension}' DE {name}\n")
        except Exception as ex:
            print(f"ERRO AO RECEBER ARQUIVO: {ex}\n")

    def send_message(self, message: str) -> None:
        if message:
            time = strftime("%H:%M")
            user_data = str(
                {
                    "name": f"{self.__name}",
                    "position": f"{self.__position}",
                    "message": f"{message}",
                }
            )
            try:
                self.__client_socket.send(user_data.encode("utf-8"))
                if message != "/sendfile":
                    print(f"Você as {time}\n{message}\n")
            except Exception as ex:
                print(f"ERRO AO ENVIAR A MENSAGEM: {ex}\n")
                self.close_client()

    def send_file(self, path_2: str):
        if path_2:
            file_path = path.join(path_2)
            file_name, file_extension = path.splitext(path_2)
            file_size = path.getsize(path_2)
            file_name = self.__shorten_name(file_name=file_name)

            file_data = str(
                {
                    "file_extension": f"{file_extension}",
                    "file_size": f"{file_size}",
                }
            )

            try:
                self.__client_socket.send(file_data.encode("utf-8"))
                with open(file_path, "rb") as file:
                    data = file.read()
                    self.__client_socket.send(data)
                print(f"ARQUIVO '{file_name}{file_extension}' ENVIADO COM SUCESSO!\n")
            except Exception as ex:
                print(f"ERRO AO ENVIAR ARQUIVO: {ex}\n")

    def close_client(self):
        self.__client_socket.close()
        print("DESCONECTADO!\n")
