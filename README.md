# Django Photoblog
Photoblog app written in Django and optimized for Heroku deployment. Uses Whitesnoise to serve static assets and Amazon S3 for user uploads.

## Requirements
- Python 3 (recommended 3.6.4)
- Django 2
- python-decouple (config variables)
- dj-database-url (database config)
- gunicorn (production server)
- psycopg2 (PostreSQL in production)
- whitenoise (static files in production)
- django-storages (media files in production)


## Features

## Running project in development


### Config Variables
Create `.env` file in `src` directory and specify config variables, e.g.:
```
SECRET_KEY=6b)c7q3g9+vxwnn3e7*m@%2=r3x6yub6stj4e9jv#4p=eita-#
DEBUG=True
DATABASE_URL=sqlite:////media/m/DATA/code/django-photoblog/src/db.sqlite3
CONTACT_FORM_EMAIL=youremail@gmail.com
BLOG_NAME=My Photoblog
```

## Heroku deployment
