import os
import environ

import dj_database_url

from django.urls import reverse_lazy

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INSTALLED_APPS = [
    "home",
    "search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "authbroker_client",
    "article",
    "storages",
    "wagtail.contrib.settings",
    "wagtailcodeblock",
    "user",
]


MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "authbroker_client.middleware.ProtectAllViewsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "authbroker_client.backends.AuthbrokerBackend",
]

LOGIN_URL = reverse_lazy("authbroker_client:login")
LOGIN_REDIRECT_URL = "/"
ROOT_URLCONF = "helpcentre.urls"

WAGTAIL_FRONTEND_LOGIN_URL = reverse_lazy("authbroker_client:login")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates"),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "helpcentre.context.shared_settings",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "helpcentre.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:postgres@postgres:5432/helpcentre"
    )
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},  # noqa: E501
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},  # noqa: E501
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},  # noqa: E501
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

WAGTAIL_SITE_NAME = "helpcentre"

BASE_URL = "http://helpcentre.datahub.gov.uk"


AUTHBROKER_URL = env.str("AUTHBROKER_URL")
AUTHBROKER_CLIENT_ID = env.str("AUTHBROKER_CLIENT_ID")
AUTHBROKER_CLIENT_SECRET = env.str("AUTHBROKER_CLIENT_SECRET")

VCAP_SERVICES = env.json("VCAP_SERVICES", {})

if "aws-s3-bucket" in VCAP_SERVICES:
    AWS_DEFAULT_ACL = None
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"
    s3 = VCAP_SERVICES["aws-s3-bucket"][0]["credentials"]
    AWS_STORAGE_BUCKET_NAME = s3["bucket_name"]
    AWS_ACCESS_KEY_ID = s3["aws_access_key_id"]
    AWS_SECRET_ACCESS_KEY = s3["aws_secret_access_key"]
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME

    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

FEEDBACK_URL = env.str("FEEDBACK_URL", "/")

SENTRY_DSN = env.str("SENTRY_DSN", None)
SENTRY_ENVIRONMENT = env.str("SENTRY_ENVIRONMENT", None)

if SENTRY_DSN:
    RAVEN_CONFIG = {"dsn": SENTRY_DSN, "environment": SENTRY_ENVIRONMENT}
    INSTALLED_APPS += ["raven.contrib.django.raven_compat"]

SHOW_ENV_BANNER = env.bool("SHOW_ENV_BANNER", False)
ENV_NAME = env.str("ENV_NAME", "")

GIT_BRANCH = env.str("GIT_BRANCH", "")
GIT_COMMIT = env.str("GIT_COMMIT", "")

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

AUTHBROKER_ANONYMOUS_PATHS = ('check', )

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "{asctime} {levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["stdout"],
        "level": os.getenv("ROOT_LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": [
                "stdout",
            ],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
        "django.server": {
            "handlers": [
                "stdout",
            ],
            "level": os.getenv("DJANGO_SERVER_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": [
                "stdout",
            ],
            "level": os.getenv("DJANGO_DB_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
    },
}

