from . import *


from .base import *
DEBUG="False"

ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        # We use the adaptater for postgresqlpostgresql
        'ENGINE': 'django.db.backends.postgresql',
        # The name of database xhose is create befor
        'NAME': 'db_cvth',
        # The user must be replave by your own name
        'USER': 'zebra3',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = environ['STATIC_ROOT']
