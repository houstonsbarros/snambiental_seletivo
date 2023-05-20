# Seletivo SN Ambiental

- [Seletivo SN Ambiental](#seletivo-sn-ambiental)
- [Introdução](#introdução)
  - [Execute o projeto](#execute-o-projeto)
- [Requisitos Gerais](#requisitos-gerais)
- [Requisitos Específicos](#requisitos-específicos)

# Introdução
O projeto é consiste na implementação de uma API REST para que possamos armazenar livros, usuários, empréstimos e seus atributos dentro de um banco de dados e realizar as operações de CRUD.

## Execute o projeto
1. Clone o repositório
``` bash
>git clone https://github.com/houstonsbarros/snambiental_seletivo.git
```

2. Extraia o arquivo

3. Acesse a pasta do projeto

4. Inicie o ambiente virtual
- Windows
``` bash
> .\venv\Scripts\activate
```
- Linux e MacOS
``` bash
> source venv/bin/activate
```

5. Instale as dependências
``` bash
>pip install -r requirements.txt
```

6. Inicie seu servidor MySQL
>Você pode utilizar o arquivo **database.sql** para criar o banco de dados.
- Verifique se o nome do seu usuário e senha são por padrão **'root'** e **''** respectivamente.
- - Se não for, altere o arquivo **settings.py** na pasta **biblioteca** e adicione seu usuário e senha.
- - - Exemplo:
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'biblioteca',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
        
    }
}
```

7. Execute as migrações
``` bash
> python manage.py makemigratios
> python manage.py migrate
```

8. Crie um usuário
``` bash
>python manage.py createsuperuser
```
> Crie o seu usuário e senha para poder obter o Token

``` javascript
{
    "username": "admin",
    "password": "1234"
}
```

![Token](https://github.com/houstonsbarros/seletivo_snambiental/assets/107281650/f50f8f44-b73b-472f-8571-20c519e92829)

![Authorization](https://github.com/houstonsbarros/seletivo_snambiental/assets/107281650/c62edba7-4760-47cc-b9e0-90bb9c2614a5)
> Copiei o token e colei no campo **Authorization** do Postman previamente adicionado como Bearer Token


9. Execute o servidor
``` bash
>python manage.py runserver
```
10. Abra o Postman e importe a collection
``` bash
> SN Ambiental.postman_collection.json
```
11.  Agora é só testar as rotas
   
# Requisitos Gerais
- [x] Implementar um mecanismo de autorização e autenticação;
- [x] Implementar os verbos post, put, get e delete para as 3 entidades;
- [x] Conter recursos de paginação em todas as consultas;
- [x] Os dados deverão ser armazenados no servidor de banco de dados previamente criado
em container ou em um banco local;
- [ ] Utilizar algum mecanismo para popular tabelas do banco de dados será um diferencial.

# Requisitos Específicos
- [x] Criar um CRUD para cada entidade preservando a relação entre as mesmas;
  
- [x] Criar um endpoint que permita consultar um livro específico por ID;
  
- [x] Criar um endpoint que permita consultar todos os empréstimos realizados por um
usuário com o ID especificado;

- [x] Criar um endpoint que permita consultar todos os empréstimos em atraso
realizados por um usuário com o ID especificado;

- [x] Criar um endpoint que permita consultar todos os empréstimos realizados entre as
datas de início e fim especificadas;