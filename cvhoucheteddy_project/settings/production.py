from . import *

SECRET_KEY = ''
DEBUG = False
ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'db_cvht', # le nom de notre base de données créée précédemment
        'USER': 'zebra385', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}