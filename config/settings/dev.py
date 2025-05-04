from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-%b_cpb&ahs8t!*4gyl(d5w@2k$@2%$du#0=ggo94-ns!6_ziy!"

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_DEBUG = True

ALLOWED_HOSTS = ["*"]

# Debug toolbar settings
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
