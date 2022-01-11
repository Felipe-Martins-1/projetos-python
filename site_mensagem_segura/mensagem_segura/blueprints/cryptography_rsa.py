# Função que valida os valores para evitar cálculo com números grandes
def validate_keys(key_1: int, key_2: int) -> bool:
    status = False
    if key_1 >= 1024 and key_1 <= 99999:
        if key_2 >= 1024 and key_2 <= 99999:
            status = True
    return status


# Função que criptografa o texto
def encrypt(text: str, key_e: int, key_n: int) -> str:

    # Retorno True
    if validate_keys(key_e, key_n):

        # Converte a string para uma lista
        text = list(text)

        for i in range(len(text)):

            # Tranforma cada caracter em um número do tipo int
            text[i] = ord(text[i])

            # Calculo da criptografia
            text[i] = (text[i] ** key_e) % key_n

            # Converte todos os valores do tipo int para o tipo string
            text[i] = str(text[i])

        # Junta todos valores da lista
        text = " ".join(text)

    # Retorno False
    else:
        text = "INVÁLIDO"
    return text


# Função que descriptografa o texto criptografado
def decrypt(text_encr: str, key_d: int, key_n: int) -> str:

    # Retorno True
    if validate_keys(key_d, key_n):

        # Cada valor da string é setado em uma lista
        text_encr = text_encr.split()

        for i in range(len(text_encr)):

            # Converte todos os valores do tipo string para o tipo int
            text_encr[i] = int(text_encr[i])

            # Calculo da descriptografia
            text_encr[i] = (text_encr[i] ** key_d) % key_n

            # Transforma todos os números do tipo int para caracteres do tipo
            # string (letras, números e pontuações)
            text_encr[i] = chr(text_encr[i])

        # Junta todos valores da lista
        text_encr = "".join(text_encr)

    # Retorno False
    else:
        text_encr = "INVÁLIDO"
    return text_encr
