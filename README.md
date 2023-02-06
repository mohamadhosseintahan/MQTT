# MQTT

In this project, we learned how to use MQTT with python 

Also we leaerned how to use redis as pup/sub system

for using this project frist clone it

```git clone git@github.com:mohamadhosseintahan/MQTT.git```

then create virtual environment with any pip package that you want

for example:
```python -m venv .env```

or:

```python virtualenv .env```

or you can use some other things like conda or pyenv or ... .

then activate the virtualenv with below command:

```source .env/bin/activate```

now you should install the requirements

```pip install -r requirements.txt```

for the last step, you should create .env file alongside core/settings.py.

you can find the sample in .envsample file.

migrate changes on DB to create log table

```python manage.py migrate```

create superuser to see the persisted logs in django admin

```python manage.py createsupseuser```

startup the celery with this command

```celery -A core worker -E -l info -B -c 3```

start the app with:

```python manage.py runserver```

and use this route in your browser to start getting data from destination MQTT

[localhost:8000/start](http://localhost:8000/start)
