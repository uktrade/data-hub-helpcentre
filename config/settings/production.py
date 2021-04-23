# flake8: noqa
from .env import *  # noqa: F403, F401

DEBUG = False

FEED_API_TOKEN = env.str("FEED_API_TOKEN")

if not FEED_API_TOKEN:
    raise ImproperlyConfigured("The FEED_API_TOKEN must not be empty")

MIDDLEWARE.append("config.middlewares.RedirectDomainMiddleware")
