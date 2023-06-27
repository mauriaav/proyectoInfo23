from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #engine = el motor
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_personal',
        'USER': 'root',
        'PASSWORD': 'Enero123+',
        'HOST': 'localhost',
        'PORT': '',
    }
}