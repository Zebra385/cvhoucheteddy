from . import *
# Parse database configuration from $DATABASE_URL
import dj_database_url
from os import environ

from .base import *
DEBUG="False"

ALLOWED_HOSTS = ['64.227.117.38']

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = environ['STATIC_ROOT']
