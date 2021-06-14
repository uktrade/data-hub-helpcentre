from .base import *  # noqa

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

CAN_ELEVATE_SSO_USER_PERMISSIONS = True
