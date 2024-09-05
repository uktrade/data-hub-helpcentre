from os import environ
from typing import Optional

import dj_database_url
from dbt_copilot_python.database import database_url_from_env
from dbt_copilot_python.network import setup_allowed_hosts
from dbt_copilot_python.utility import is_copilot
from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .cf_env import CloudFoundryEnvironment


class DBTPlatformEnvironment(BaseSettings):
    """Class holding all environment variables for HELPCENTRE.

    Environment variables all have a prefix of "HELPCENTRE_"
    e.g. HELPCENTRE_DJANGO_DEBUG == DBTPlatformEnvironment.django_debug (not case-sensitive)
    """

    model_config = SettingsConfigDict(
        env_prefix="HELPCENTRE_",
        extra="ignore",
        validate_default=False,
    )

    build_step: bool = Field(alias="build_step", default=False)

    django_debug: bool

    secret_key: str
    allowed_hosts: list[str]

    authbroker_client_id: str
    authbroker_client_secret: str
    authbroker_url: str
    oauthlib_insecure_transport: int = 0

    feed_api_token: str = ""
    feedback_url: str = "/"

    # Optional - url to sentry endpoint
    sentry_dsn: Optional[str] = None
    sentry_environment: Optional[str] = None

    # Hawk credentials
    hawk_incoming_access_key: str = ""
    hawk_incoming_secret_key: str = ""

    # git
    git_branch: Optional[str] = ""
    git_commit: Optional[str] = ""

    # S3 env vars
    aws_region: str = Field(alias="aws_region", default="")
    aws_storage_bucket_name: str = Field(alias="aws_storage_bucket_name", default="")

    env_name: Optional[str] = ""
    show_env_banner: Optional[bool] = False

    @computed_field  # type: ignore[misc]
    @property
    def allowed_hosts_list(self) -> list[str]:
        if self.build_step:
            return self.allowed_hosts

        # Makes an external network request so only call when running on DBT Platform
        return setup_allowed_hosts(self.allowed_hosts)

    @computed_field  # type: ignore[misc]
    @property
    def database_config(self) -> dict:
        if self.build_step:
            return {"default": {}}

        return {
            "default": dj_database_url.parse(database_url_from_env("DATABASE_CREDENTIALS")),
        }

    @computed_field  # type: ignore[misc]
    @property
    def s3_bucket_config(self) -> dict:
        """Return s3 bucket config that matches keys used in CF"""

        if self.build_step:
            return {"aws_region": "", "bucket_name": ""}

        return {"aws_region": self.aws_region, "bucket_name": self.aws_storage_bucket_name}

if is_copilot():
    if "BUILD_STEP" in environ:
        # When building use the fake settings in .env.circleci
        env: DBTPlatformEnvironment | CloudFoundryEnvironment = DBTPlatformEnvironment(
            _env_file=".env", _env_file_encoding="utf-8"
        )  # type:ignore[call-arg]
    else:
        # When deployed read values from environment variables
        env = DBTPlatformEnvironment()  # type:ignore[call-arg]
else:
    # Cloud Foundry environment
    env = CloudFoundryEnvironment(_env_file=".env", _env_file_encoding="utf-8")  # type:ignore[call-arg]