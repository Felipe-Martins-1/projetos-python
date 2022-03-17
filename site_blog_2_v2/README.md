# site_blog
- ATUALIZAÇÃO (V1 para V2):
    - Duas extensões do Flask foram acrescentadas ao projeto, sendo o Flask-Login e o Flask-Admin, uma biblioteca para o login e a outra para a interface de administrador.

- DESCRIÇÃO:
    - Este projeto é um aplicativo web utilizando o microframework Flask;
    - Contém interface de administrador;
    - Cadastra novos usuários;
    - Atualiza nome e senha do usuário;
    - Tem as funções de login e logout com diferentes permissões;
    - Adiciona, atualiza e deleta postagens;
    - Mostra todas os textos postados;
    - Possuí duas API's, uma retorna todos os usuários e a outra retorna todas as postagens.

- OBSERVAÇÕES:
    - Suporta um texto de até 1500 caracteres;
    - Banco de dados: SQLite;
    - Para demonstração, no banco de dados já tem alguns dados cadastrados de usuários para login ("vini", "ryan", "maria", "lara" e a senha de todos é "123") e postagens, também há um usuário/administrador (adm, senha "890");
    - No arquivo ".env" a variável de ambiente "FLASK_ENV" deste projeto recebe o valor "production", indicado para ambiente de produção (depurador do Flask desligado), já para ambiente de desenvolvimento a variável recebe o valor "development" (depurador do Flask ligado).

- INSTALAÇÕES NECESSÁRIAS:
    - Python 3.8.0;
    - Flask 2.0.2;
    - Flask-Admin 1.6.0;
    - Flask-Login 0.5.0;
    - Flask-Migrate 3.1.0;
    - Flask-SQLAlchemy 2.5.1;
    - Werkzeug 2.0.3;
    - dynaconf 3.1.7;
    - python-dotenv 0.19.2.

- PARA INICIAR O APP:
    - Abra o terminal;
    - Entre no diretório raiz do projeto;
    - Digite o comando "venv\Scripts\activate" para ativar o ambiente virtual;
    - Ative o servidor com o comando "flask run" e para desativar o servidor aperte "CTRL C";
    - Abra o navegador e acesse a URL "http://localhost:5000/" ou "http://127.0.0.1:5000/".

- DESENVOLVEDOR RESPONSÁVEL:
    - Felipe Martins (github.com/Felipe-Martins-1).