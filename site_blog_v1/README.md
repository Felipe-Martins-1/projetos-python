# site_blog

- DESCRIÇÃO:
    - Este projeto é um aplicativo web utilizando o microframework Flask;
    - Cadastra novos usuários;
    - Tem as funções de login e logout com diferentes permissões;
    - Adiciona, atualiza e deleta postagens;
    - Mostra todas os textos postados;
    - Possuí duas API's, uma retorna todos os usuários (.../api-json/usuarios) e a outra retorna todas as postagens (.../api-json/postagens).

- OBSERVAÇÃO:
    - Suporta um texto de até 1500 caracteres;
    - Banco de dados: SQLite;
    - No banco de dados já tem alguns dados cadastrados de usuários, para login (vini, ryan, mari, lara e a senha de todos é "123") e postagens para demostração;
    - No arquivo ".env" a variável de ambiente "FLASK_ENV" deste projeto recebe o valor "production", indicado para ambiente de produção (depurador do Flask desligado), já para ambiente de desenvolvimento a variável recebe o valor "development" (depurador do Flask ligado).

- INSTALAÇÃO:
    - Python 3.8.0;
    - Flask 2.0.2;
    - Flask-Migrate 3.1.0;
    - Flask-SQLAlchemy 2.5.1;
    - Werkzeug 2.0.3;
    - dynaconf 3.1.7;
    - python-dotenv 0.19.2.

- INICIAR APP:
    - Abra o terminal;
    - Entre no diretório raiz do projeto;
    - Digite o comando "venv\Scripts\activate" para ativar o ambiente virtual;
    - Ative o servidor com o comando "flask run" e para desativar o servidor aperte "CTRL C";
    - Abra o navegador e acesse a URL "http://localhost:5000/" ou "http://127.0.0.1:5000/".