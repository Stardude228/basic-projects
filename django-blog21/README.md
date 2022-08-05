# Django project Blog
## commands
> `django-admin startproject config .` - creates a project, if we put a dot in the end the project will be created in this folder, if we do not the project will create a folder named config and will startproject there
> `python manage.py startapp name_of_app` - creates an app
> `python manage.py makemigrations` - checks all models if there are any changes creates a new file in migrations with changes
> `python manage.py migrate` - check all files related to migrations and changes tables in database
> `python manage.py runserver` - lauches our project on 127.0.0.1:8000
> `python manage.py runserver 5000` - lauches our project on 127.0.0.1:5000

## settings.py
* BASE_DIR - root folder of our project
* SECRET_KEY - secret key
* DEBUG - if True, all errors will be displayed, that's why on production it will be False
* ALLOWED_HOSTS - Available hosts to host our project on (if list is empty it will be hosted on localhost(127.0.0.1))
* INSTALLED_APPS - All apps that our project will be using
* MIDDLEWARE - All middlewares(functions that process requests) that our project will be using
* ROOT_URLCONF - The main file urls
* DATABASES - The settings of databases that our project will be using

## how request is processed
1. wsgi/asgi (accept the request and return answer)
2. settings -> middlewares (process our request)
3. urls (router that checks url and if there are any matches send the request to required function (views))
4. views (functions that return data in correct format)
5. serializers (classes that transform data from json into objects from models and reversely)
6. models (classes that show how our table and what columns do we have)
7. managers (objects) (classes that work with ORM that have methods for creation, updating, deletion and recieving filter of records from table)
8. database

