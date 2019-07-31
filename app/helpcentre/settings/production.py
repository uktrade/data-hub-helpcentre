from .base import *  # noqa: F403, F401
from django.core.exceptions import ImproperlyConfigured

DEBUG = False

if not FEED_API_TOKEN:
    raise ImproperlyConfigured('The FEED_API_TOKEN must not be empty')

try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass
