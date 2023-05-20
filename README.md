# Shop

Django shop project

## Quick start

In your command line:
```
git clone https://github.com/RomanLezhaiko/graduate_work_tms.git
cd graduate_work_tms
```

Create virtual enviroment:
```
python3 -m venv .venv

source .venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Change database settings in shop/settings/base.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '', # name of database
        'USER': '', # user of db
        'PASSWORD': '', # password for db
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Run migrate
```
cd shop

python manage.py migrate
```

Fill the db:
```
python manage.py loaddata category.json

python manage.py loaddata products.json

python manage.py loaddata products_image.json

python manage.py loaddata users.json
password for admin: admin
```

Run the app:
```
python manage.py runserver
```

Install Redis if it is not present on your operating system, and after write in new terminal
```
redis-server --port 7777
```

In new terminal activate venv and write next lines
```
cd shop

python3 -m celery -A shop worker -l INFO
```


P.S. for running test
1. Enable redis: redis-server --port 7777