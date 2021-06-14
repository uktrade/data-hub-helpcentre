from django_log_formatter_ecs import ECSFormatter

from .base import *  # noqa


INSTALLED_APPS += [  # noqa F405
    "elasticapm.contrib.django",
]

MIDDLEWARE += [
    "config.middlewares.RedirectDomainMiddleware",
    "django_audit_log_middleware.AuditLogMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ELASTIC_APM = {
    "SERVICE_NAME": "DataHub Help Centre",
    "SECRET_TOKEN": env("ELASTIC_APM_SECRET_TOKEN"),  # noqa F405
    "SERVER_URL": env("ELASTIC_APM_SERVER_URL"),  # noqa F405
    "ENVIRONMENT": env("APP_ENV"),  # noqa F405
    "SERVER_TIMEOUT": env("ELASTIC_APM_SERVER_TIMEOUT", default="20s"),  # noqa F405
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "ecs_formatter": {"()": ECSFormatter,},
        "simple": {"format": "{asctime} {levelname} {message}", "style": "{",},
    },
    "handlers": {
        "ecs": {"class": "logging.StreamHandler", "formatter": "ecs_formatter",},
        "simple": {"class": "logging.StreamHandler", "formatter": "simple",},
    },
    "root": {
        "handlers": ["ecs", "simple",],
        "level": os.getenv("ROOT_LOG_LEVEL", "INFO"),  # noqa F405
    },
    "loggers": {
        "django": {
            "handlers": ["ecs", "simple",],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),  # noqa F405
            "propagate": False,
        },
        "django.server": {
            "handlers": ["ecs", "simple",],
            "level": os.getenv("DJANGO_SERVER_LOG_LEVEL", "ERROR"),  # noqa F405
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["ecs", "simple",],
            "level": os.getenv("DJANGO_DB_LOG_LEVEL", "ERROR"),  # noqa F405
            "propagate": False,
        },
    },
}
