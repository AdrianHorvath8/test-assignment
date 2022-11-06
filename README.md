# Test_assignment

I created a application that takes data from json file save them into models and displays them.

## Getting Started


### Prerequisites

You need to have installed [Python](https://www.python.org/downloads/), [VScode](https://code.visualstudio.com/Download), [PostgreSQL](https://www.postgresql.org/download/) and [PgAdmin](https://www.pgadmin.org/download/)


### Installing

* clone repo 
* create a virtual environment and activate
  * 1 - mkdir .venv   |=>  into root directory
  * 2 - python -m venv .venv
  * 3 - source .venv/Scripts/activate
* pip install -r requirements.txt
* open project in VScode with **code .**  command
* set up your postgresql database
* put information about your database into the settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "database_name",
        'USER': "user",
        'PASSWORD': "user_password",
        'HOST': "localhost",
        'PORT': '5432',
    }
}
```
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Django](https://docs.djangoproject.com) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - Used to web APIs
* [PostgreSQL](https://www.postgresql.org/) - Database used
* [PgAdmin](https://www.pgadmin.org/) - Used for managing database
* [Postman](https://www.postman.com/) - Used for APIs documentation

## Features

* Importing data
* Seeing data by model name
* Seeing data by model name and Id


## Versioning

I use [Git](https://git-scm.com/) for versioning

## Links

*  [API documentation](https://documenter.getpostman.com/view/18653876/2s8YYFr3fh)
 

## Authors

* *Adrián Horváth* - *Backend work* 
