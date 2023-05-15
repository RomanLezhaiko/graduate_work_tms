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

Run the app:
```
cd shop

python3 manage.py runserver
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






P.S. For deploy version
1. change DEBUG in setting to False
2. change static url, root
3. collectstatic
4. runserver