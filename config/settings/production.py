# flake8: noqa
from django.core.exceptions import ImproperlyConfigured

from .env import *

DEBUG = False

FEED_API_TOKEN = settings_env.feed_api_token

if not FEED_API_TOKEN:
    raise ImproperlyConfigured("The FEED_API_TOKEN must not be empty")

MIDDLEWARE += [
    "config.middlewares.RedirectDomainMiddleware",
    "django_audit_log_middleware.AuditLogMiddleware",
]

INSTALLED_APPS += [
    "django_audit_log_middleware",
]

# Audit log middleware user field
AUDIT_LOG_USER_FIELD = "username"
