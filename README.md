# mysite-django app

* turorial for django project

* https://docs.djangoproject.com/en/2.0/intro/tutorial01/

* python 2.7

* django 1.11.12

### list command

* run project:

`python manage.py runserver`

* add polls app:

`python manage.py startapp polls`

* make change with the database from polls model:

`python manage.py makemigrations polls`

* apply change db:

`python manage.py migrate`

* watch sql create polls model:

`python manage.py sqlmigrate polls 0001`

* start dev shell:

`python manage.py shell`

* create admin user: (localhost:8000/admin---admin/ab798979)

`python manage.py createsuperuser`

* test:

`python manage.py test polls`
