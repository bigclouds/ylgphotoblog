# Django Photoblog
Photoblog app written in Django. Features photo tagging and simple CMS for creating pages with WYSIWYG editor. Ready for Heroku deployment. Uses Whitesnoise to serve static assets and Amazon S3 for photo uploads.

## Requirements
- Python 3 (recommended 3.6.4)
- Django 2
- django-tagging
- django-ckeditor
- django-widget-tweaks
- easy_thumbnails
- python-decouple
- dj-database-url
- gunicorn (production)
- psycopg2 (production)
- Whitenoise (production)
- boto3 (production)
- django-storages (production)

## Features
- photo tagging using django-tagging
- infinite scrolling on the list views
- gallery view using carousel in modal window
- thumbnail generation using easy_thumbnails
- CMS for creating pages with CKEditor
- enabled widget-tweaks for better form styling
- database config with dj-database-url
- config variables with python-decouple
- optimized for Heroku deployment with gunicorn
- production static file serving with Whitenoise
- production media file service with Amazon S3


### Config variables
Create `.env` file in `src` directory and specify your development settings, e.g.:
```
BLOG_NAME=Photoblog
BLOG_DESCRIPTION=Photographer portfolio app powered by Django.
CONTACT_FORM_EMAIL=youremail@gmail.com
CONTACT_PAGE_TITLE=Contact me
CONTACT_PAGE_SLUG=contact-me
TAG_CLOUD_LIMIT=10
SEO_NOINDEX=False
SOCIAL_PROFILES=True
FACEBOOK_URL=https://facebook.com/yourfacebookprofile
TWITTER_URL=https://twitter.com/yourtwitterprofile
PINTEREST_URL=https://pinterest.com/yourpinterestprofile
LINKEDIN_URL=https://linkedin.com/yourlinkedinprofile

SECRET_KEY=6b)c7q3g9+vxwnn3e7*m@%2=r3x6yub6stj4e9jv#4p=eita-#
DEBUG=True
DATABASE_URL=sqlite:////media/m/DATA/code/django-photoblog/src/db.sqlite3
```
