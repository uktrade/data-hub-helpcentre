from .base import *  # noqa: F403, F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "helpcentre",}}

try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass
