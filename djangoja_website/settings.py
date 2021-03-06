# Settings for djangoja_website project.

import os
import json
import platform
from unipath import FSPath as Path

BASE = Path(__file__).absolute().ancestor(2)

# Far too clever trick to know if we're running on the deployment server.'
PRODUCTION = ('DJANGOPROJECT_DEBUG' not in os.environ) and ("djangoproject" in platform.node())

ENVS = json.load(open(BASE.child('environments.json')))
SECRET_KEY = str(ENVS['secret_key'])

ADMINS = (
    ('hirokiky', 'hirokiky@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Asia/Tokyo'
LANGUAGE_CODE = 'ja'

if PRODUCTION:
    DEBUG = False
    MEDIA_URL = "https://www.djangoproject.jp/m/"
    ADMIN_MEDIA_PREFIX = "https://www.djangoproject.jp/m/admin/"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangoprojectjp',
            'USER': ENVS['db_default_user'],
            'PASSWORD': ENVS['db_default_password'],
            'HOST': ENVS['db_default_host'],
            'PORT': ENVS['db_default_port'],
        }
    }

else:
    DEBUG = True
    MEDIA_URL = "/media/"
    ADMIN_MEDIA_PREFIX = '/admin_media/'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE.child('development.db'),
        }
    }

TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_ROOT = BASE.child('djangoja_website').child('media')
TEMPLATE_DIRS = BASE.child('djangoja_website').child('templates')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'djangoja_website.urls'

WSGI_APPLICATION = 'djangoja_website.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'sphinxdoc',
    'haystack',
    'django.contrib.comments',
    'tagging',
    'mptt',
    'zinnia',
)

HAYSTACK_SITECONF = 'djangoja_website'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = BASE.child('whoosh_index')

ZINNIA_MARKUP_LANGUAGE = 'restructuredtext'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
