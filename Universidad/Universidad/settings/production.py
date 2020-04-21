from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cuarentasemanas.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2f5jggrnej8a8',
        'USER': 'seqapevgjsmefx',
        'PASSWORD': '0098e32dd78dbd3aaab191910e1aa655b0e6252f5fd1e2a9ad24aadcb5eead85',
        'HOST': 'ec2-52-71-85-210.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


