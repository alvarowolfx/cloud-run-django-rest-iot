# settings_dev.py

from .settings import *

DEBUG = True
SECRET_KEY = 'itbtx53x$rzm@j5*l9ct07up7n6$m99r_thd3m&+$&8l6+4cgj'

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')

if os.getenv('DB_NAME', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            'USER': f"{DB_USER}",
            'PASSWORD': f"{DB_PASS}",
            'NAME': f"{DB_NAME}",
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
