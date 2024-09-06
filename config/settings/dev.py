from config.env import *  # noqa: F403, F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
