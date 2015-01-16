import dj_database_url
import os

#from django.utils.translation import ugettext_lazy as _
_ = lambda s: s


DEBUG = os.environ.get('DEBUG', True)
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '$6(x*g_2g9l_*g8peb-@anl5^*8q!1w)k&e&2!i)t6$s8kia94'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']


ROOT_URLCONF = 'thinkster_django_angular_boilerplate.urls'
WSGI_APPLICATION = 'thinkster_django_angular_boilerplate.wsgi.application'
AUTH_USER_MODEL = 'authentication.Account'


INSTALLED_APPS = (
    'djangocms_admin_style',
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'compressor',
    'thinkster_django_angular_boilerplate.authentication',
    'thinkster_django_angular_boilerplate.posts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
)

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'django_thinkster',
    #    'USER': 'django',
    #    'PASSWORD': 'postgres',
    #    'HOST': 'localhost',
    #    'PORT': '5432',
    #}
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}

ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:authentication_account_changelist',
                'title': _('Users'),
            },
            {
                'url_name': 'admin:posts_post_changelist',
                'title': _('Posts'),
            },
        ]
    },
]
