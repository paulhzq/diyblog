# Step by step how to create the diyblog.

## Install python3, pip and virtualenv.

## Create a fold to store the project.

> mkdir diyblog

> cd diyblog

## create a virtualenv for our project.
> virtualenv diyblog_env

## activate the virtualenv.
> source diyblog_env/bin/activate

or

> ./diyblog_env/bin/activate

## Install the django package.
> pip install django
### Want to freeze all the dependency module to a file.
> pip freeze > requirement.txt
### So next time when other people can use the same env as yours just using the command
> pip install -r requirement.txt

## Create the new project using the django-admin
> django-admin startproject diyblog .

Don't forget the . in the end otherwise you will have 3 diyblog fold eventually.

## Run the diyblog application.
> python manage.py runserver

Open the browser and check: localhost:8000
