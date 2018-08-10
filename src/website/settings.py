import os

import dj_database_url
from decouple import config


# Blog config
BLOG_NAME = config('BLOG_NAME', default='Photoblog')
BLOG_DESCRIPTION = config('BLOG_DESCRIPTION', default=None)
CONTACT_FORM_EMAIL = config('CONTACT_FORM_EMAIL')
CONTACT_PAGE_TITLE = config('CONTACT_PAGE_TITLE', default='Contact')
CONTACT_PAGE_SLUG = config('CONTACT_PAGE_SLUG', default='contact')
CONTACT_PAGE_DESCRIPTION = config(
    'CONTACT_PAGE_DESCRIPTION',
    default='Send me a message using the form below.')
TAG_CLOUD_LIMIT = config('TAG_CLOUD_LIMIT', default=10, cast=int)
RELATED_TAGS_LIMIT = config('RELATED_TAGS_LIMIT', default=5, cast=int)
SEO_BLOG_TITLE = config('SEO_BLOG_TITLE', default=None)
SEO_BLOG_DESCRIPTION = config('SEO_BLOG_DESCRIPTION', default=None)
SEO_NOINDEX = config('SEO_NOINDEX', default=False, cast=bool)
SOCIAL_PROFILES = config('SOCIAL_PROFILES', default=False, cast=bool)
DEVIANTART_URL = config('DEVIANTART_URL', default=None)
GOOGLEPLUS_URL = config('GOOGLEPLUS_URL', default=None)
FACEBOOK_URL = config('FACEBOOK_URL', default=None)
INSTAGRAM_URL = config('INSTAGRAM_URL', default=None)
LINKEDIN_URL = config('LINKEDIN_URL', default=None)
PINTEREST_URL = config('PINTEREST_URL', default=None)
TUMBLR_URL = config('TUMBLR_URL', default=None)
TWITTER_URL = config('TWITTER_URL', default=None)
TAGS_FORMAT = "%Y-%m-%d"

# General config
ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# LoginUrl
LOGIN_URL="/admin/login/"


# Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=500,
    )
}


# Email backend
if DEBUG:
    #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_USE_TLS = False
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = config('EMAIL_PORT')
else:
    EMAIL_USE_TLS = True
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = config('EMAIL_PORT')


# App config

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'blog.apps.BlogConfig',
    'videos.apps.VideosConfig',
    'contact_form.apps.ContactFormConfig',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'tagging',
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.nav_processor',
                'blog.context_processors.config_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'src/static')


STATIC_ROOT1 = os.path.join(BASE_DIR, 'html5media')
STATIC_URL1 = '/html/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]

# S3 Media Storage
if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    DEFAULT_FILE_STORAGE = 'website.storage_backends.MediaStorage'
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE  # easy_thumbnails
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    AWS_QUERYSTRING_AUTH = False


# Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'medium': {'size': (500, 500), 'crop': True},
        'carousel': {'size': (800, 800), 'crop': False},
    },
}


# CKEditor
CKEDITOR_BROWSE_SHOW_DIRS = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_UPLOAD_PATH = ""
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Maximize', 'Format', 'Bold', 'Italic', 'Underline', '-', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor', 'Image', 'Embed', '-'],
            ['Undo', 'Redo', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo', 'Find', 'Replace', '-', 'SelectAll', '-', 'Source']
        ],
        'height': 400,
        'width': '100%',
        'extraPlugins': ','.join(
            [
                'image2',
                'embed',
            ]),
        'language': 'en',
    },
}
