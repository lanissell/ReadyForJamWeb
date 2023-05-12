import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-k2ngvej3n3(u#6mdj1up6b$37$hvl0f!fblf&borpe0rs6c)kg'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'login',
    'jam',
    'project',
    'ckeditor',
    'ckeditor_uploader',
    'jinja2',
    'debug_toolbar',
    'jquery',
    'django_node_assets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ROOT_URLCONF = 'ReadyForJam.urls'
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        'OPTIONS': {
            'environment': 'ReadyForJam.jinja2.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ReadyForJam.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ReadyForJamDb',
        'USER': 'superuser',
        'PASSWORD': 'fekod24rfFF',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

NOTIFICATIONS_USE_JSONFIELD = True

LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ('node_modules', os.path.join(BASE_DIR, 'node_modules/')),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_node_assets.finders.NodeModulesFinder',
]

NODE_MODULES_ROOT = os.path.join(BASE_DIR, 'node_modules')

NODE_PACKAGE_JSON = os.path.join(BASE_DIR, 'package.json')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTO_LOGOUT = {'SESSION_TIME': 600}

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Custom': [
            {'name': 'document', 'items': ['Source', 'Preview']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'links', 'items': ['Youtube']},
            {'name': 'insert',
             'items': ['Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', ]},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'toolbar': 'Custom',  # put selected toolbar config here
        'toolbarGroups': [{'name': 'document', 'groups': ['mode', 'document', 'doctools']}],
        'height': 200,
        'width': '100%',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'skin': 'moono-lisa',
        'extraPlugins': ','.join([
            # your extra plugins here
            'youtube',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
        ]),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


