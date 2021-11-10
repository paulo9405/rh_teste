# Desafio RH

Boa tarde!, para esse desafio recomendamos conhecimento basico em alguns frameworks e python!

  - Django
  - Pip
  - Python 3x
  - Html
  - Css
  - Javascript

# Vamos Lá!

para começar siga alguns passos:

  - Fork esse diretorio
  - Clone para o seu computador
  - Crie sua venv!
  - instale os requirementos utilizando o pip (requirements.txt)
  - Pronto! podemos começar!


Vamos avaliar nesse teste:
  - Velocidade de execução (60%)
  - Qualidade do algoritimo (30%)
  - Novas melhorias no algoritimo (10%)

Caso tenha qualquer duvida a respeito do teste pode me chamar aqui mesmo no git! ou no [linkedin](https://www.linkedin.com/in/wr-rek/)

### Observações

> Utilize sempre a seguinte padronização, Model > Django Admin > |View <> Url| > Template
> Esse teste envolve apenas o desenvolvimento dos CRUDS
> Qualquer outra inclusão além do CRUD entrará como bonus.
> Para entregar o projeto basta apenas devolver o link do repositorio para a Monire
> Caso queira realizar o "deploy da aplicação" somará mais pontos! e se for no HEROKU! mais pontos ainda :)

### Chega de enrolações e vamos aos algoritimos

O desafio consiste em um sistema basico de RH, nele temos as empresas (company) os departamentos (department) dessas empresas e seus colaboradores (employee)

Temos os models dessas já setados porém você terá que adicionar alguns campos a mais para as empresas e para os departamentos e para os Colaboradores!

### Para a Empresa (Company)!

| Campo | Tipo |
| ------ | ------ |
| logo | ImageField |
| name | CharField|
| legal_number | CharField |

### Para o Departamento (Department)!

| Campo | Tipo |
| ------ | ------ |
| company | ForeignKey - Company |
| name | CharField|
| status | BooleanField |
| Admin | UUIDField ou ForeignKey - User |

### Para o Colaborador (Employee)!
| Campo | Tipo |
| ------ | ------ |
| department | ForeignKey - Department |


### Estrutura Url

| Model | Url |
| ------ | ------ |
| Employee | [company/employee/] |
| Company | [company/]|
| Department | [company/deparment/] |

### ADMIN

| Model |
| ------ |
| Employee
| Company |
| Department |

# Importante

#### Faça a View do Employee com todos os campos do template, e não esqueça de colocar também a foto da empresa no template, confirá todos os campos, Não esqueça do CRUD COMPLETO nas views, porém no template apenas o Insert(Create  ou C do CRUD).

#### O create user, update user, são campos de UUID referentes ao usuário de criação e são auto preenchidos no momento do cadastro no TEMPLATE, (não avaliaremos o cadastro do django admin) consideraremos um extra! :)

### Dicas!
###### Não esqueçam!, de realizar as migrações corretamente ou o teste não irá funcionar, makemigrations, migrate, a view está na pasta template/core/user_form, recomendo usar para a View a versão generatica! mas caso queira usar based in model, fique avontade!


### Colas!

```sh
Git
$ git add .
$ git commit -m "Comentario"
$ git push origin main
Python
Criar a Virtual Env
$ virtualenv venv
Ativar a venv
$ . venv/Scripts/activate
Instalar os Requerimentos:
$ pip install -r requirements.txt
Iniciar as Migrações
$ python manage.py makemigrations
Aplicar as Migrações
$ python manage.py migrate
Criar um super usuário (Django Admin/ Django Auth)
$ python manage.py createsuperuser
Rodar o servidor!
$ python manage.py runserver
```

## Vamos lá!!



