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
mkdir heroku_deploy && cd $_
git init
python3 -m venv venv
source venv/bin/activate
pip install django django-heroku
pip freeze > requirements.txt
git add .
git commit -m 'Init Commit'
```
Once we've setup our dependencies, we create the requirements.txt file that Heroku will use to configure the app. Heroku expects one of [three possible files](https://devcenter.heroku.com/articles/deploying-python#expected-files-for-python) to manage dependencies. 


### Create your Django Project and App

```python
django-admin startproject django_project_name .
python manage.py startapp django_app_name
```

I'm using very explicit names so that your other configuration files will be self-documenting, i.e. `from django_app_name import views`

### Create a minimum viable Django app
I will omit the full details of this step, but you will need to add a view, register your app in settings.py, and add whatever path you prefer to use. You should be able to run `python manage.py runserver` and view a page other than the default Django splash page at `localhost:8000`. This is a good time to appreciate that you just knocked out a Django application.

## Heroku
======

### Preparing your application for Heroku
Here we start to touch upon a little Heroku magic for deploying your application. We'll need to do two things.
1. Create the Heroku application that connects Heroku to your Django project
2. Create the Procfile that defines how your app is started on Heroku's servers
3. Configure `django-heroku` to handle launching your app on Heroku

## Creating your Heroku application
There is [a lot of support for deploying Python applications on Heroku](https://devcenter.heroku.com/categories/python-support), but we'll be able to accomplish this with a one to two commands.

```
heroku login
heroku create
```

This should create a Heroku application with a randomly assigned name initialized to the current directory. You can manage your applications from the CLI or [your Heroku application dashboard](https://dashboard.heroku.com/apps).

## Creating your Procfile
The second step for deploying on Heroku will be creating your Procfile. [The Procfile](https://devcenter.heroku.com/articles/procfile) is how Heroku launches your application. The basic unit of the Procfile is a process type and a command.

```
<process type>: <command>
```

For example:
```
web: python manage.py runserver 0.0.0.0:$PORT
```

You will most likely be using the [web process type](https://devcenter.heroku.com/articles/procfile#the-web-process-type) for your deployments. This is a special process type that is able to receive web traffic, and it will be responsible for running your app. I recommend starting with this Procfile for your Django application:

```
web: python manage.y runserver 0.0.0.0:$PORT
```

This will use the default Django development server to launch your application bound to an address and port accessible to Heroku. You should be familiar with most of this command already. We've added two things to make it function on Heroku:
1. We bound the address to something other than 127.0.0.1/localhost, which is not accessible from the web
2. We bound the port to the Heroku environment variable `$PORT` instead of the default (and also forbidden) 8000.

These two steps allow our development server to function on the open web.

## Configuring `django-heroku`
Open your `settings.py` file under `/django_project_name/` and add the following two lines: one at the top with your other imports and one near the bottom.

```python
import django_heroku
...

...
django_heroku.settings(locals())
```

This will configure Heroku's [django-heroku library](https://github.com/heroku/django-heroku) which magically handles some secrets, databases, and the collection of static files in the background.

### Red, Green, Refactor

## Pushing and deploying
I strongly recommend testing locally with `python manage.py runserver` until you are confident that the Django side of your application is locked down before deploying to Heroku. This helps you identify what is a Django issue vs. what is a Heroku config issue. Once you're ready to attempt deployment, we use git to push to heroku

```
git push heroku master
... A lot of text will appear
heroku open
```

Once you push your repo to heroku, it will attempt to automatically determine how to launch your application based on available files and your Procfile configuration. Once you're done building your application, you can use `heroku open` to open your application in a new browser window! You should now either have a deployed Django application on the open web or a good place to start troubleshooting. 

### Troubleshooting your Heroku deployment

## Check the Heroku logs
You can use `heroku logs --tail` to see the logs from your application. This will expose Heroku logging messages, which feature [very helpful error codes](https://devcenter.heroku.com/articles/error-codes), and things like the stack trace for your app if it crashes.  

## Common Errors

1. `Error while running '$ python manage.py collectstatic --noinput'` - `django_heroku` isn't configured correctly
2. `H14 - No web dynos running` - If you're following along, you probably need to fix your Procfile
