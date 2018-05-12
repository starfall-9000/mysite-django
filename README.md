# mysite-django app

* turorial for django project

* https://docs.djangoproject.com/en/1.11/intro/tutorial01/

* python 2.7

* django 1.11.12

### learning

* create a module, router with urls, create templates, create module and database

* use admin site localhost:8000/admin

* create python package https://docs.djangoproject.com/en/1.11/intro/reusable-apps/

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

* template render test enviroment:

```
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

* build packages:

`python setup.py sdist`
