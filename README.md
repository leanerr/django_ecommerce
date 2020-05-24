# django_ecommerce
its a shop or ecommerce website by using django. 
i used django-shop-tutorial but i will try to add new features and also change the admin-panel lang to persian.
the zarin-pal payment is added.
# django-project

## Setup

### Install Django:
```bash
pip install Django
```

### Perform database migration:
```bash
python manage.py check
python manage.py migrate
```

## Run Development Server

```bash
python manage.py runserver
```
Public endpoint is at http://localhost:8000/polls/

Admin endpoint is at http://127.0.0.1:8000/admin/, `user: admin`, `password: qazwsxedc`

## Testing

### Run tests:
```bash
python manage.py test
```

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.025s

OK
Destroying test database for alias 'default'...
```

### Run tests with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
```

### Check coverage report:
```bash
coverage report
```

```bash
Name                                Stmts   Miss  Cover
-------------------------------------------------------
manage.py                              13      6    54%
mysite/__init__.py                      0      0   100%
mysite/settings.py                     18      0   100%
mysite/urls.py                          3      0   100%
mysite/wsgi.py                          4      4     0%
polls/__init__.py                       0      0   100%
polls/admin.py                          4      0   100%
polls/apps.py                           4      0   100%
polls/migrations/0001_initial.py        7      0   100%
polls/migrations/__init__.py            0      0   100%
polls/models.py                        20      1    95%
polls/templates/__init__.py             0      0   100%
polls/templates/polls/__init__.py       0      0   100%
polls/tests.py                         57      0   100%
polls/urls.py                           4      0   100%
polls/views.py                         28      8    71%
-------------------------------------------------------
TOTAL                                 162     19    88%
```

