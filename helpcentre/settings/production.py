from .base import *  # noqa: F403, F401
from django.core.exceptions import ImproperlyConfigured

DEBUG = False

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

FEED_API_TOKEN = env.str("FEED_API_TOKEN")
if not FEED_API_TOKEN:
    raise ImproperlyConfigured("The FEED_API_TOKEN must not be empty")

try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass

MIDDLEWARE.append("helpcentre.middlewares.RedirectDomainMiddleware")
