from pathlib import Path
import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', cast=bool, default=True)

# Security

SECRET_KEY = '#!#28d#+2y0-n3b^@85r8&ygh60i+k-j@x#$oa+ednd^&qf(0('

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'rest_framework_simplejwt',
    'todoapp',
    'todoapp.applications.account',
    'todoapp.applications.todo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'todoapp/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todoapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todoapp',
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='5449'),
        'USER': 'postgres',
        'PASSWORD': config('DATABASE_PASSWORD', default='todoapp'),
        'ATOMIC_REQUESTS': True
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth

AUTH_USER_MODEL = 'account.User'

# Session

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_COOKIE_AGE = timedelta(days=360).total_seconds()

# AWS

AWS_ACCESS_KEY_ID = 'TODO'

AWS_SECRET_ACCESS_KEY = 'TODO'

AWS_DEFAULT_REGION = 'eu-south-1'

# AWS S3

AWS_S3_ADDRESSING_STYLE = 'virtual'

AWS_STORAGE_BUCKET_NAME = 'todoapp'

AWS_S3_SIGNATURE_VERSION = 's3v4'

AWS_S3_REGION_NAME = AWS_DEFAULT_REGION

AWS_DEFAULT_ACL = 'public-read'

AWS_QUERYSTRING_AUTH = False

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age={},public'.format(int(timedelta(weeks=8).total_seconds()))
}

AWS_LOCATION = 'media'

# Media files

DJANGO_SERVE_MEDIA = DEBUG

if DJANGO_SERVE_MEDIA:

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))

    MEDIA_URL = '/media/'

else:

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Drf

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'JSON Web Token authentication': {
            'type': 'jwt'
        }
    }
}
