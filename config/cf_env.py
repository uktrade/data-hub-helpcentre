from typing import Annotated, Any, Optional

from dbt_copilot_python.database import database_url_from_env
import dj_database_url
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PostgresDsn,
    TypeAdapter,
    computed_field,
)
from pydantic.functional_validators import PlainValidator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Convert the database_url to a PostgresDsn instance
def validate_postgres_dsn_str(val: str) -> PostgresDsn:
    return TypeAdapter(PostgresDsn).validate_python(val)


CFPostgresDSN = Annotated[PostgresDsn, PlainValidator(validate_postgres_dsn_str)]


class VCAPServices(BaseModel):
    model_config = ConfigDict(extra="ignore")
    aws_s3_bucket: list[dict[str, Any]] = Field(alias="aws-s3-bucket")
    postgres: list[dict[str, Any]]
    redis: list[dict[str, Any]]


class CloudFoundryEnvironment(BaseSettings):
    """Class holding all environment variables for Helpcentre.

    Instance attributes are matched to environment variables by name (ignoring case).
    e.g. CloudFoundryEnvironment.app_name loads and validates the APP_NAME  environment variable.
    """

    model_config = SettingsConfigDict(
        extra="ignore",
        validate_default=False,
    )

    database_url: CFPostgresDSN

    # Cloud Foundry Environment Variables
    vcap_services: VCAPServices | None = None

    # Start of Environment Variables
    secret_key: str = Field(alias="helpcentre_secret_key")
    allowed_hosts: list[str] = Field(alias="helpcentre_allowed_hosts")
    django_debug: bool = Field(alias="helpcentre_debug", default=False)

    authbroker_client_id: str = Field(alias="helpcentre_authbroker_client_id")
    authbroker_client_secret: str = Field(alias="helpcentre_authbroker_client_secret")
    authbroker_url: str = Field(alias="helpcentre_authbroker_url")
    oauthlib_insecure_transport: int = Field(alias="helpcentre_oauthlib_insecure_transport", default=0)

    feed_api_token: str = Field(alias="helpcentre_feed_api_token", default="")
    feedback_url: str = Field(alias="helpcentre_feedback_url", default="/")

    # Optional - url to sentry endpoint
    sentry_dsn: Optional[str] = Field(alias="helpcentre_sentry_dsn", default=None)
    sentry_environment: Optional[str] = Field(alias="helpcentre_sentry_environment", default=None)

    # Hawk credentials
    hawk_incoming_access_key: str = Field(alias="helpcentre_hawk_incoming_access_key", default="")
    hawk_incoming_secret_key: str = Field(alias="helpcentre_hawk_incoming_secret_key", default="")

    # git
    git_branch: Optional[str] = Field(alias="helpcentre_git_branch", default="")
    git_commit: Optional[str] = Field(alias="helpcentre_git_commit", default="")

    # S3 env vars
    aws_region: str = Field(alias="aws_region", default="")
    aws_storage_bucket_name: str = Field(alias="aws_storage_bucket_name", default="")

    app_name: Optional[str] = Field(alias="helpcentre_app_name", default="")
    show_env_banner: Optional[bool] = Field(alias="helpcentre_show_env_banner", default=False)

    @computed_field  # type: ignore[misc]
    @property
    def allowed_hosts_list(self) -> list[str]:
        return self.allowed_hosts

    @computed_field  # type: ignore[misc]
    @property
    def database_config(self) -> dict:
        return {"default": dj_database_url.parse(str(self.database_url))}


    @computed_field  # type: ignore[misc]
    @property
    def s3_bucket_config(self) -> dict:
        if self.vcap_services:
            app_bucket_creds = self.vcap_services.aws_s3_bucket[0]["credentials"]
        else:
            app_bucket_creds = {}

        return app_bucket_creds