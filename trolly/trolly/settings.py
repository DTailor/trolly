from os.path import abspath, basename, dirname, join, normpath
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)

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
    'gunicorn',
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

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'trolly', 'templates')),
)

MEDIA_ROOT = normpath(join(SITE_ROOT, 'trolly', 'media'))

MEDIA_URL = '/media/'
STATIC_ROOT = normpath(join(SITE_ROOT, 'trolly', 'assets'))

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'trolly', 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


try:
    from local_settings import *
except ImportError:
    pass
