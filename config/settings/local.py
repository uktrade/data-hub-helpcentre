import environ
import os

from .base import *  # noqa

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

CAN_ELEVATE_SSO_USER_PERMISSIONS = True
