This will be the README instructions for deploying a Django app to Heroku
======

This is a short tutorial in creating and deploying a Django application on Heroku. The goal is to be able to quickly move an existing local Django application to a free Heroku deployment using the django_heroku library. We will then move from the Django development server to Gunicorn to provide another example of configuring your Procfile.

## Before Starting

1. Create an account with [Heroku](https://www.heroku.com/)
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## Setup a Django Application

```python

python3 -m venv venv
source venv/bin/activate
pip install django django-heroku
```
