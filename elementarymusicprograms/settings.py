import os
from danemco.autosite.common_settings import *
# the default settings are set in common_settings. 
# This allows us to make changes to all settings pages easily and removes the
# amount of code that is needed in this settings file 

DIRNAME = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(DIRNAME, '..', 'media')
STATIC_ROOT = os.path.join(DIRNAME, '..', 'media', "static")

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)

DATABASE_NAME = 'elementarymusicprograms'
DATABASE_USER = 'elementarymusicp'
DATABASE_PASSWORD = '98f0669a1019f613e841040fb298aafb'

SECRET_KEY = 'bb%9ii3+z@3t%_i!5q4^l@a_d1m2=kt8k6n%y_0hp5s(0cp(09'

ROOT_URLCONF = 'elementarymusicprograms.urls'

DEFAULT_FROM_EMAIL = 'elementarymusicprograms <info@elementarymusicprograms.com>'
DEFAULT_CONTACT_EMAIL = 'elementarymusicprograms <info@elementarymusicprograms.com>'

INSTALLED_APPS = (
    'staticfiles',
    'compressor',
    'danemco.misc',
    'danemco.apps.autodoc',
    'danemco.apps.treemenus',
    'danemco.dash',
    'danemco.uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'sorl.thumbnail',
    'danemco.mini_shop',
    'danemco.themes.current',
    'danemco.gallery',
    'danemco.newsletter',
    'danemco.mini_shop.extensions.addresses',
    'danemco.mini_shop.extensions.authorize',
    'danemco.mini_shop.extensions.order_emails',
    'danemco.mini_shop.extensions.regions',
    'danemco.mini_shop.extensions.statistics',    
)


COMPRESS_URL = MEDIA_URL
PAGINATE_GALLERY_BY = 10
RECENT_PHOTOS_TO_SHOW = 5
COMPRESS_ROOT = MEDIA_ROOT

VELOCITY_SITE = False

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
    '/opt/django-stuff1.0/danemco/themes/current/templates/',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'danemco.context_processors.danemco_media',
    'danemco.themes.context_processors.theme_url',
    'django.core.context_processors.auth',
    'staticfiles.context_processors.static',
)
STATICFILES_FINDERS = (
    'staticfiles.finders.FileSystemFinder',
    'staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


CAPTCHA = {
    'bgcolor': '#FFFFFF',
    'fgcolor': '#000000',
}

#===============================================================================
# Allow danemco customizations such as adding default apps
try:
    from danemco.utils.update_settings import update
    update(globals())
except Exception, ex:
    logging.error("Exception modifying default settings", exc_info=True)
# end danemco customizations
#===============================================================================

# custom override settings hook
from danemco.autosite.override_settings import *
