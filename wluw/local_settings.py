LASTFM_API_KEY = 'caf527c3fa125943c0744326e3ee1d84'
LASTFM_API_SECRET = 'fdafba40277dc4972b4e31c5126ff7b6'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wluw',                      # Or path to database file if using sqlite3.
        'USER': 'wluw',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEBUG=True
TEMPLATE_DEBUG=DEBUG

CELERY_DEFAULT_EXCHANGE = "tasks"
CELERY_RESULT_BACKEND = 'database'
CELERY_RESULT_DBURI = 'wluw://postgres@localhost/wluw'

CELERY_IMPORTS = ('wluw.radio.library.tasks',)

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_VHOST = "/"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"

