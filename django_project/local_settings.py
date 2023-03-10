import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-14vti6x+r6isbdi9q4)lm4tdsx3*9ag0vdl(6u1*!8sf_%t2c-'

#settings.pyからそのままコピー
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = True