import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'faver'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'trolly.urls'

WSGI_APPLICATION = 'trolly.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )


MEDIA_ROOT = (os.path.join(BASE_DIR, 'faver', 'media'))

MEDIA_URL = '/media/'

STATIC_ROOT = (os.path.join(BASE_DIR, 'faver', 'static'))

STATIC_URL = '/static/'


try:
    from local_settings import *
except ImportError:
    pass
