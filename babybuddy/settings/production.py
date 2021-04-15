from .base import *

# Production settings
# See babybuddy.settings.base for additional settings information.

SECRET_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'babybuddy',
        'USER': 'babybuddy@gitdbserv',
        'PASSWORD': 'DBPASSWORD',
        'HOST': 'gitdbserv.postgres.database.azure.com',
        'PORT': '5432',
    }
}


# Media files
# https://docs.djangoproject.com/en/3.0/topics/files/

MEDIA_ROOT = os.path.join(BASE_DIR, '../data/media')
