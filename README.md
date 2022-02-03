# Back-end Challenge 🏅 2021 - Space Flight News

### API REST Criada como projeto de desafio para o teste da Coodesh.
A API possui sistema de paginação e utiliza autenticação via token, permitindo apenas leitura para usuários não autenticados e consome os dados da API Original Space Flight News utilizando chamadas assincronas para verificar com melhor performance se há novos artigos na API original e fazer o update ou criação de novos artigos caso seja necessário.

## Endpoints
### Space Flight API 
```
http://127.0.0.1:8000/articles - Retorna lista com todos os artigos da API - Aceita metodos GET/POST
http://127.0.0.1:8000/articles/<id>/ - Retorna artigo com o id informado - Aceita metodos GET/PUT/DELETE
```

```
Porta padrão é 8000, mas pode ser alterada na inicialização do servidor (Descrito abaixo).
```

#### Parametros
| Nome   |      Tipo      |  Descrição | Obrigatório
|:----------:|:-------------:|:----------:|:------:|
| id |  Int | Id do artigo desejado | Não


## Guia de uso

### Clonar o repositório:
```
git clone https://github.com/gustavopirro/SpaceFlightAPI.git
```
### Entrar na pasta do projeto
```
cd caminho/do/projeto
```

### Baixar e instalar dependências:
```
pip install -r requirements.txt
```

### Crie o arquivo 'local_settings.py' dentro do diretório 'mysite'.

### Gere e copie uma SECRET_KEY neste site:
[https://djecrety.ir/](https://djecrety.ir/)


### No local_settings.py crie a variável 'SECRET_KEY' e atribua a ela a key gerada anteriormente:
```
SECRET_KEY = 'key_gerada' 
```

## Configuração do Banco de Dados PostgreSQL:
### Com o banco PostgreSQL instalado na maquina local, adicione o código abaixo, substituindo os valores de name, host, port, user e password no local_settings.
### Lembre-se de criar o banco de dados no SGBD do PostgreSQL.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_banco',
        'HOST': 'host_postgresql',
        'PORT': 'porta',
        'USER': 'usuario_postgresql',
        'PASSWORD': 'senha',
    }
}
```

### Com o terminal aberto na pasta raiz do projeto deve se executar o comando para fazer as migrações:
```
python manage.py migrate
```

### Rodando o servidor de forma local, com o terminal na pasta raiz do projeto executar o comando:
```
python manage.py runserver
```
### Caso a porta 8000 esteja ocupada é necessário informar outra porta a ser utilizada:
```
python manage.py runserver 127.0.0.1:porta_desejada
```
