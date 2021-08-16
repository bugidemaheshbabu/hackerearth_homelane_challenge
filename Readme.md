This project has done as a part of **HomeLane Backend Hiring Challenge** on HackerEarth


The application is developed by using Django Framework

Run this by
```
python3.8 virtualenv env
pip install -r requirements.txt
python3.8 manage.py migrate
python3.8 manage.py makemigrations core
python3.8 manage.py runserver
```


The search fields are taken as path parameters
The localhost Urls
```
http://localhost:8080/core/get-pinpoint-state/Bihar/2021-8-14/

http://localhost:8080/core/get-state-info/Bihar/ 

http://localhost:8080/core/get-date-info/2021-08-15/
```

The Project tree is as given below

```
├── core # Main App
│   ├── admin.py
│   ├── apps.py
│   ├── datasets
│   │   ├── covid_19_india.csv
│   │   ├── covid_vaccine_statewise.csv
│   │   └── StatewiseTestingDetails.csv
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── populate_dataset.py  # Read the csv data and dump into database using bulk_create()
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── db.sqlite3
├── homelane_covid_19_3rd_wave_prev # Project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Procfile.txt  # Heroku Deployment file
└── requirements.txt
```


Tasks Completed

- Data Populated in SQLite
- Written 3 Query service APIs
- Deployed to Heroku
- Performed UnitTesting

