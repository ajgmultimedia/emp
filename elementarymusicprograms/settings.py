import os
from danemco.autosite.common_settings import *
# the default settings are set in common_settings. 
# This allows us to make changes to all settings pages easily and removes the
# amount of code that is needed in this settings file 

DIRNAME = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(DIRNAME, '..', 'media')
STATIC_ROOT = os.path.join(DIRNAME, '..', 'media', "static")

ROOT_URLCONF = 'elementarymusicprograms.urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)
DEBUG = False
VELOCITY_SITE = False
DATABASE_NAME = 'elementarymusicprograms'
DATABASE_USER = 'elementarymusicp'
DATABASE_PASSWORD = '98f0669a1019f613e841040fb298aafb'
DEFAULT_FROM_EMAIL = 'elementarymusicprograms <emp4kids@gmail.com>'
DEFAULT_CONTACT_EMAIL = 'elementarymusicprograms <emp4kids@gmail.com>'
SECRET_KEY = 'bb%9ii3+z@3t%_i!5q4^l@a_d1m2=kt8k6n%y_0hp5s(0cp(09'
DATABASE_HOST = '10.0.0.254'


#satchmo_store.shop
SATCHMO_HTML_EMAILS = True
from danemco.utils.satchmo.defaults import *
SATCHMO_SETTINGS.update({
    'SHOP_BASE': '/shop',
    'MULTISHOP': False,
    'SHOP_AJAX_CHECKOUT': True
})

#danemco.misc
SITE_NAME = "Elementary Music Programs"

#compressor
COMPRESS_PRECOMPILERS = (
     ('text/less', 'lessc {infile} {outfile}'),
 )
if not DEBUG:
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
        ]

COMPRESS_URL = MEDIA_URL
COMPRESS_ROOT = MEDIA_ROOT


INSTALLED_APPS = (
    'staticfiles',
    'compressor',
    'danemco.misc',
    'danemco.apps.autodoc',
    'danemco.apps.social',
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
    
    # Satchmo Store
    'comment_utils',
    'danemco.flex_shipping',
    'danemco.quickdata',
    'danemco.quickdata.modules.product',
    'danemco.newreports',
    'satchmo_store.shop',
    'livesettings',
    'l10n',
    'satchmo_store.contact',
    'satchmo_ext.productratings',
    'satchmo_ext.shopper_groups',
    'satchmo_ext.measured_products',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    'shipping.modules.tiered',
    'shipping.modules.tieredweight',
    'product',
    'payment',
    'payment.modules.giftcertificate',
    'satchmo_utils',
    'satchmo_store.accounts',
    'app_plugins',
    'danemco.apps.trackingcode',
    'danemco.quickdata.modules.contact',
    'keyedcache',
    'mptt',
    'registration', 
    'satchmo_ext.affiliates',
    'satchmo_ext.checkout_questions',
    'satchmo_ext.class_products',
    'satchmo_ext.email_contact',
    'satchmo_store.contact.supplier',

    'satchmo_ext.quickcart',
    'danemco.reports',
    'danemco.apps.office_dash',    
        
    'danemco.themes.current',
    'danemco.apps.treemenus',
    'danemco.gallery',
    'danemco.newsletter',
    'satchmo_ext.upsell',

    #'danemco.mini_shop',
    #'danemco.mini_shop.extensions.addresses',
    #'danemco.mini_shop.extensions.authorize',
    #'danemco.mini_shop.extensions.order_emails',
    #'danemco.mini_shop.extensions.regions',
    #'danemco.mini_shop.extensions.statistics',    
)

PAYPAL_LIVE=True
PAYPAL_EMAIL="tavacischool@gmail.com"
PAGINATE_GALLERY_BY = 15
RECENT_PHOTOS_TO_SHOW = 5

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
    os.path.join(DANEMCO_DIR, 'themes/current/templates'),
#    '/opt/django-stuff1.0/danemco/themes/current/templates/',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'satchmo_store.shop.SSLMiddleware.SSLRedirect',
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
    'satchmo_store.shop.context_processors.settings',
    'staticfiles.context_processors.static',
)
STATICFILES_FINDERS = (
    'staticfiles.finders.FileSystemFinder',
    'staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'satchmo_store.accounts.email-auth.EmailBackend',
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
#from danemco.autosite.override_settings import *
