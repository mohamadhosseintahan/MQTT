# MQTT

In this project, we learned how to use MQTT with python 

Also we leaerned how to use redis as pup/sub system


## Virtual Environment
create virtual environment with any pip package that you want

for example:

```python -m venv .env```

or:

```python virtualenv .env```

or you can use any alternatives.

then activate the virtualenv with below command:

```source .env/bin/activate```


## Requirements
now, you should install the requirements

```pip install -r requirements.txt```

then, you should create .env file alongside core/settings.py.

you can find the sample in .envsample file.

migrate changes on DB to create log table:

```python manage.py migrate```

## Celery
startup the celery with this command:

```celery -A core worker -E -l info -B -c 3```

## Main App
start the app with:

```python manage.py runserver```

and use this route in your browser to start getting data from destination MQTT

[localhost:8000/start](http://localhost:8000/start)
