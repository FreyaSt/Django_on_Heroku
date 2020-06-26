This will be the README instructions for deploying a Django app to Heroku
======

This is a short tutorial in creating and deploying a Django application on Heroku. The goal is to be able to quickly move an existing local Django application to a free Heroku deployment using the django_heroku library. We will then move from the Django development server to Gunicorn to provide another example of configuring your Procfile.

## Before Starting

1. Create an account with [Heroku](https://www.heroku.com/)
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## Setup a Django Application

### Initial Environment
Create your virtual environment, activate it, and install Django and the django-heroku dependency used in this tutorial.

```python

python3 -m venv venv
source venv/bin/activate
pip install django django-heroku
pip freeze > requirements.txt
```
Once we've setup our dependencies, we create the requirements.txt file that Heroku will use to configure the app. Heroku expects one of [three possible files](https://devcenter.heroku.com/articles/deploying-python#expected-files-for-python) to manage dependencies.


### Create your Django Project and App

```python
django-admin startproject django_project_name .
python manage.py startapp django_app_name
```

I'm using very explicit names so that your other configuration files will be self-documenting, i.e. `from django_app_name import views`

### Create a minimum viable Django app
I will omit the full details of this step, but you will need to add a view, register your app in settings.py, and add whatever path you prefer to use. You should be able to run `python manage.py runserver` and view a page other than the default Django splash page at `localhost:8000`.




