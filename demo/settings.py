import os
from typing import List, Dict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+fh&pb@89zq##pk&ozsfidi!yn2o$fy)ptp$^4gh#3cx%^@9i_'
DEBUG = True
ALLOWED_HOSTS: List[str] = []
STATIC_ROOT = BASE_DIR + '/demo/static/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'js_logger',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'demo/static/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

JS_LOGGER = {'CONSOLE_LOG_LEVEL': 'INFO', 'CONSOLE_ERROR_LEVEL': 'WARNING'}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'simple': {'format': '%(levelname)s %(name)s -- %(message)s'}},
    'handlers': {'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}},
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG'},
        'django': {'handlers': ['console'], 'level': 'INFO', 'propagate': True},
        'django.server': {'handlers': ['console'], 'level': 'INFO', 'propagate': False},
        'django.request': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False},
        'console_log': {'handlers': ['console'], 'level': JS_LOGGER['CONSOLE_LOG_LEVEL']},
        'console_error': {'handlers': ['console'], 'level': JS_LOGGER['CONSOLE_ERROR_LEVEL']},
    },
}

REST_FRAMEWORK: Dict[str, str] = {}
