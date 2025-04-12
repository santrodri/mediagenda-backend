# Mediagenda (Backend)

## Motivação
Este projeto pretende demonstrar meus conhecimentos em Python. Ele será construído gradualmente integrado com um frontend.

Esse aplicativo conta com autenticação por JWT e envio de email para confimação de autenticidade.
## Como Iniciar o Projeto
Você pode baixar este repositório e executar os seguintes comandos:

### Requisitos
- python3.12

### Passos
1. Instale as dependências: O exemplo mostrado será para sistemas unix baseados no Debian
    ```bash
    python3.12 -m venv venv
    source venv/bin/activate 
   ```
   
2. Instale as dependencias do projeto:
    ```bash
   pip install -r requeriments.txt
   ```

3. Execute as migrações e execute o projeto.
    ```bash
       python manage.py makemigrations
       python manage.py migrate
       python manage.py runserver
    ```

Sinta-se à vontade para usar este projeto livremente, sugerir melhorias ou entrar em contato comigo pelo e-mail: `ogirdo.sant@gmail.com`.

## Imagens do projeto
* Pagina de documentação
    ![documentacao da api](/readme/Captura%20de%20tela%20de%202025-04-11%2021-41-34.png)
    essa pagina é gerada por bibliotecas integradas ao codigo garantindo a sincrionia de codigo com documentação
    
* Email enviado ao cliente
    ![imagen de tela de cadastro](readme/Captura%20de%20tela%20de%202025-04-11%2021-55-59.png)
    Essa paginá e enviada ao cliente como forma de autencação do email