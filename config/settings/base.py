import os
import sys

import dj_database_url
from dbt_copilot_python.utility import is_copilot
from django_log_formatter_asim import ASIMFormatter
from django.urls import reverse_lazy

from config.env import env as settings_env

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DEBUG = settings_env.django_debug

SECRET_KEY = settings_env.secret_key

ALLOWED_HOSTS = settings_env.allowed_hosts_list

CSRF_TRUSTED_ORIGINS = settings_env.csrf_trusted_origins

INSTALLED_APPS = [
    "home",
    "search",
    "inline_feedback",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.table_block",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "authbroker_client",
    "article",
    "storages",
    "wagtail.contrib.settings",
    "wagtailcodeblock",
    "user",
    "sass_processor",
    "rest_framework",
    "api_v1",
    "api_pipeline",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "authbroker_client.middleware.ProtectAllViewsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "user.backends.CustomAuthbrokerBackend",
]

LOGIN_URL = reverse_lazy("authbroker_client:login")
LOGIN_REDIRECT_URL = "/"
ROOT_URLCONF = "config.urls"

WAGTAIL_FRONTEND_LOGIN_URL = reverse_lazy("authbroker_client:login")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context.shared_settings",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:postgres@postgres:5432/helpcentre"  # /PS-IGNORE
    )
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },  # noqa: E501
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },  # noqa: E501
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },  # noqa: E501
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True


USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend"),
    os.path.join(BASE_DIR, "node_modules/govuk-frontend/govuk"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

WAGTAIL_SITE_NAME = "helpcentre"

WAGTAILADMIN_BASE_URL = "http://helpcentre.datahub.gov.uk"

AUTHBROKER_URL = settings_env.authbroker_url
AUTHBROKER_CLIENT_ID = settings_env.authbroker_client_id
AUTHBROKER_CLIENT_SECRET = settings_env.authbroker_client_secret

# AWS S3
app_bucket_creds = settings_env.s3_bucket_config
AWS_REGION = app_bucket_creds.get("aws_region")
AWS_STORAGE_BUCKET_NAME = app_bucket_creds.get("bucket_name")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


if not is_copilot():
    # Only required in Cloud Foundry.
    AWS_ACCESS_KEY_ID = app_bucket_creds.get("aws_access_key_id")
    AWS_SECRET_ACCESS_KEY = app_bucket_creds.get("aws_secret_access_key")

FEEDBACK_URL = settings_env.feedback_url

SENTRY_DSN = settings_env.sentry_dsn
SENTRY_SAMPLE_RATE = settings_env.sentry_sample_rate
SENTRY_ENVIRONMENT = settings_env.sentry_environment

if SENTRY_DSN is not None:
    RAVEN_CONFIG = {"dsn": SENTRY_DSN, "environment": SENTRY_ENVIRONMENT, "sample_rate": SENTRY_SAMPLE_RATE}
    INSTALLED_APPS += ["raven.contrib.django.raven_compat"]

SHOW_ENV_BANNER = settings_env.show_env_banner
ENV_NAME = settings_env.app_env

GIT_BRANCH = settings_env.git_branch
GIT_COMMIT = settings_env.git_commit

HAWK_INCOMING_ACCESS_KEY = settings_env.hawk_incoming_access_key
HAWK_INCOMING_SECRET_KEY = settings_env.hawk_incoming_secret_key

AUTH_USER_MODEL = "user.User"

# https://github.com/FlipperPA/wagtailcodeblock#languages-available
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ("bash", "Bash/Shell"),
    ("css", "CSS"),
    ("diff", "diff"),
    ("html", "HTML"),
    ("javascript", "Javascript"),
    ("json", "JSON"),
    ("python", "Python"),
    ("r", "R"),
    ("scss", "SCSS"),
    ("yaml", "YAML"),
)

WAGTAIL_CODE_BLOCK_THEME = None

# Add a custom provider
# Your custom provider must support oEmbed for this to work. You should be
# able to find these details in the provider's documentation.
# - 'endpoint' is the URL of the oEmbed endpoint that Wagtail will call
# - 'urls' specifies which patterns
ms_stream_provider = {
    "endpoint": "https://web.microsoftstream.com/oembed",
    "urls": [
        "^https://.+?.microsoftstream.com/video/.+$",
    ],
}
# https://*.microsoftstream.com/video/ID
# https://web.microsoftstream.com/video/2db4eeae-f9f8-4324-997a-41f682dea240 /PS-IGNORE

# Need a custom youtube provider because the Wagtail default has a bug
youtube_provider = {
    "endpoint": "https://www.youtube.com/oembed",
    "urls": [
        "^https://www.youtube.com/watch.+$",
    ],
}

WAGTAILEMBEDS_FINDERS = [
    {
        "class": "wagtail.embeds.finders.oembed",
        "providers": [
            youtube_provider,
            ms_stream_provider,
        ],
    }
]

AUTHBROKER_ANONYMOUS_PATHS = (
    "check",
    "/api/feeds/data-hub/updates/",
    "/api/pipeline/user-inline-feedback-survey",
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"},
        "asim_formatter": {
            "()": ASIMFormatter,
        },
    },
    "handlers": {
        "asim": {
            "class": "logging.StreamHandler",
            "formatter": "asim_formatter",
            "stream": sys.stdout,
        },
    },
    "root": {
        "handlers": ["asim"],
        "level": os.getenv("ROOT_LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": [
                "asim",
            ],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "django.server": {
            "handlers": [
                "asim",
            ],
            "level": os.getenv("DJANGO_SERVER_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": [
                "asim",
            ],
            "level": os.getenv("DJANGO_DB_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
