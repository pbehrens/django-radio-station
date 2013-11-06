
import os



import djcelery
djcelery.setup_loader()

BROKER_URL = 'amqp://guest:guest@localhost:5672/'


ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_CONTEXT_PROCESSORS = (
    #"django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "radio.station.context_processors.google_analytics",
    "radio.station.context_processors.current_datetime",
    "radio.frontend.context_processors.today",
	"django.contrib.auth.context_processors.auth",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#STATIC_ROOT = '/Users/thebeagle/dev/django/django-radio-station/wluw/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
# STATIC_URL = '/admin_media/'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
	os.path.join(os.path.dirname(__file__), 'static_files'),
)

ADMIN_MEDIA_PREFIX = '/static/grappelli/'

# Don't share this with anybody.
SECRET_KEY = 'y3cpni&%g-v-)qge&^dj@9u*fw_ety%4duxgrt#w$5o#b0@_+4'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'wluw.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.markup',
	'django.contrib.staticfiles',
    'south',
    'radio.frontend',
    'radio.events',
    'radio.library',
    'radio.logs',
    'radio.station',
    'radio.staff',
	'radio.content',
    'gravatar',
    'djcelery',
    'gunicorn',
    'sorl.thumbnail',

	# 'filebrowser',
	# 'tinymce',

    #'djcelery',
#    'gunicorn',
#	'filebrowser',
#    'tinymce',

)

TEMPLATE_LOADERS = (
    #'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	
    # 'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)
# AUTHENTICATION_BACKENDS = (
# 	'django.contrib.auth.backends.ModelBackend',
# )
# 
# 
# SESSION_COOKIE_DOMAIN = 'localhost'
AUTH_PROFILE_MODULE = 'radio_station.DJ'
SITE_ID = 1

NODE_PORT = 8124

#tiny mce stuff
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_FILEBROWSER = True

#filebrowser
FILEBROWSER_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
#FILEBROWSER_MEDIA_ROOT = '/Volumes/files/thebeagle/dev/django/django-radio-station/wluw/media'
FILEBROWSER_MEDIA_URL = '/media'
FILEBROWSER_DIRECTORY = 'upload/'


import django.template
django.template.add_to_builtins('django.templatetags.future')

try:
    from local_settings import *
except ImportError:
    pass
