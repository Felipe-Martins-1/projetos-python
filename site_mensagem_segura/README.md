# site_mensagem_segura

- DESCRIÇÃO:
    - Este projeto é um aplicativo web utilizando o microframework Flask;
    - Criptografa e descriptografa textos digitadas pelo usuário;
    - Gera chaves válidas;
    - Baseado na lógica da "Criptografia RSA".

- OBSERVAÇÃO:
    - A descriptografia de palavras com acentuação apresenta erros, portanto considerar palavras sem acentuação;
    - As chaves públicas são "N" e "E";
    - A chave privada é "D";
    - No arquivo ".env" a variável de ambiente "FLASK_ENV" deste projeto recebe o valor "production", indicado para ambiente de produção (depurador do Flask desligado), já para ambiente de desenvolvimento a variável recebe o valo "development" (depurador do Flask ligado).

- Instalação:
    - Python 3.8.0;
    - Flask 2.0.2;
    - dynaconf 3.1.7;
    - python-dotenv 0.19.2.

- Iniciar o app:
    - Abra o terminal;
    - Entre no diretório raiz do projeto;
    - Ative o servidor com o comando "flask run", para desativar o servidor aperte "CTRL C";
    - Abra o navegador e acesse a URL "http://localhost:5000/" ou "http://127.0.0.1:5000/".