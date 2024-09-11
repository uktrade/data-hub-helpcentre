from typing import Annotated, Any, Optional

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


class VCAPApplication(BaseModel):
    model_config = ConfigDict(extra="ignore")

    application_id: str
    application_name: str
    application_uris: list[str]
    cf_api: str
    limits: dict[str, Any]
    name: str
    organization_id: str
    organization_name: str
    space_id: str
    uris: list[str]


class VCAPServices(BaseModel):
    model_config = ConfigDict(extra="ignore")
    aws_s3_bucket: list[dict[str, Any]] = Field(alias="aws-s3-bucket")
    postgres: list[dict[str, Any]]


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
    vcap_application: VCAPApplication | None = None
    vcap_services: VCAPServices | None = None

    # Start of Environment Variables
    secret_key: str
    allowed_hosts: list[str] | str
    django_debug: bool = False

    authbroker_client_id: str
    authbroker_client_secret: str
    authbroker_url: str

    elastic_apm_secret_token: str = ""
    elastic_apm_server_timeout: str = "20s"
    elastic_apm_server_url: str = ""

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
    aws_region: str = ""
    aws_storage_bucket_name: str = ""

    app_env: Optional[str] = ""
    show_env_banner: Optional[bool] = False

    @computed_field  # type: ignore[misc]
    @property
    def allowed_hosts_list(self) -> list[str]:
        if isinstance(self.allowed_hosts, str):
            return [host.strip() for host in self.allowed_hosts.split(",") if host.strip()]
        return  self.allowed_hosts

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
