IT_blog
=======
It will be awesome blog but now it`s in development.
<hr>

Requirements
------------

All you need - to clone repository, have python (python3 recommended), create virtual environment in project folder:

    $ python3 -m venv env_name

install there dependencies:

    $ . env_name/bin/activate
    $ pip install -r requirements.txt

Then collect PostgreSQL server (you can use guide from https://djbook.ru/examples/77/ instead of couple next points.
WARNING: use user and password den - 1234 and database name - it_blog or change them on yours in settings.py):

    $ sudo apt-get install postgresql postgresql-server-dev-9.5

open postgres console:

    $ sudo -u postgres psql postgres

create administrator with password and create new user and database for the project:

    $ create user den with password 1234;
    $ create database it_blog owner den;
    $ \q

Finally do migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

then create superuser for the project:

    $ python manage.py createsuperuser

and run:

    $ python manage.py runserver

ready! Go to 127.0.0.1:8000 and enjoy)
<hr>
