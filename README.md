# Iniciando um projeto em python

## Criando ambiente virtual 
python -m venv .venv

### Ativando ambiente virtual
- Windows: .\.venv\Scripts\activate
- Linux: 

# Instalando Django
pip install Django

## Criar arquivo de dependências do projeto
pip freeze > requirements.txt

## Para instalar as dependências
pip install -r ./requirements.txt

## Criando projeto Django
No Django temos um relacionamento 1:N ou seja um projeto tem várias aplicações

django-admin startproject nome-do-projeto

ou criar os arquivos dentro de uma pasta já existente 

navegue até a pasta e rode:
django-admin startproject nome-do-projeto .

## Executando o projeto
python manage.py runserver

# Criando aplicação
python manage.py startapp products

# Trabalhando com migrations

## Gerar a migração
python manage.py makemigrations

## Rodar a migração
python manage.py migrate