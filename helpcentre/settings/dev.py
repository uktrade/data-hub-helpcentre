import os
import sys
from .base import *  # noqa: F403, F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "1jj%#-0z&2iyfh+8*1&86#tv(4e6tyq^x0+a$^5kr7)hj%9ce%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "stdout": {"class": "logging.StreamHandler", "stream": sys.stdout,},
        "null": {"class": "logging.NullHandler",},
    },
    "root": {"handlers": ["stdout"], "level": os.getenv("ROOT_LOG_LEVEL", "INFO"),},
    "loggers": {
        "django": {
            "handlers": ["stdout",],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
        "wagtail.core": {
            "handlers": ["stdout",],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
        "django.server": {"handlers": ["null"], "propagate": False,},
    },
}
