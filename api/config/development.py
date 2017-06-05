from .base import *

APP_ENV = 'development'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME', 'api_django'),
        'USER': os.environ.get('DATABASE_USER', 'root'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'root'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '3306'),
    },
}
