"""
Django settings for manager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ic3r)q^l+pzz4*yxkn(e$!j-g!6lvb-n2=dae16+y$oer7)!1l'

# Project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(
    os.path.join(__file__, os.path.pardir)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'manager.apps.main',
    'manager.apps.brand',
    'compressor',
    'south',
    'tastypie',
    'captcha',
    'haystack'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'manager.urls'

WSGI_APPLICATION = 'manager.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Default timezone
# https://docs.djangoproject.com/en/dev/ref/settings/#time-zone

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# Use timezones
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz

USE_TZ = True

# Subsite configuration

SUBSITE = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

#JS
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
    'compressor.filters.template.TemplateFilter'
]

# Template loaders
# https://github.com/SyrusAkbary/pyjade#django

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Compress configuration
# http://django-compressor.readthedocs.org/en/master/remote-storages/using-sta
# ticfiles

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

COMPRESS_ENABLED = True
COMPRESS_AUTO = True
COMPRESS_VERSION = True
COMPRESS_OFFLINE = False
COMPRESS_PARSER = 'compressor.parser.LxmlParser'
COMPRESS_OUTPUT_DIR = ''
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'

# CSS
COMPRESS_CSS_HASHING_METHOD = 'hash'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.template.TemplateFilter'
]

# Server email
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'noreply@okfn.org'

# Static files finders
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATICFILES_F
# INDERS

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # http://django-compressor.readthedocs.org/en/master/quickstart/
    'compressor.finders.CompressorFinder',
)

# Template context processors
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processo
# rs

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "manager.context_processors.site"
)

# Password hashers : for more password security
# https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-bcrypt-
# with-django

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# Logo size (for brand, brandowner, and brandproposal images)
LOGO_SIZE = (150, 150)
LOGO_FORMAT = 'jpeg'

# Upload limitation
TASK_UPLOAD_FILE_TYPES = ['image']
TASK_UPLOAD_FILE_MAX_SIZE = 102400

# Django haystack
# https://django-haystack.readthedocs.org/en/latest/signal_processors.html#real
# time-realtimesignalprocessor
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
