# Django Photoblog
Photoblog app written in Django. Features photo tagging and simple CMS for creating pages with WYSIWYG editor. Ready for Heroku deployment. Uses Whitesnoise to serve static assets and Amazon S3 for photo uploads.

## Requirements
- Python 3 (recommended 3.6.4)
- Django 2
- django-tagging
- django-ckeditor
- django-widget-tweaks
- python-decouple
- dj-database-url
- gunicorn (production)
- psycopg2 (production)
- whitenoise (production)
- django-storages (production)

## Features

## Running project in development

### Config variables
Create `.env` file in `src` directory and specify your development settings, e.g.:
```
SECRET_KEY=6b)c7q3g9+vxwnn3e7*m@%2=r3x6yub6stj4e9jv#4p=eita-#
DEBUG=True
DATABASE_URL=sqlite:////media/m/DATA/code/django-photoblog/src/db.sqlite3
CONTACT_FORM_EMAIL=youremail@gmail.com
BLOG_NAME=My Photoblog
```

## Heroku deployment
