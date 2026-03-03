from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class AuthenticationService(BaseSettings):
    user_name: SecretStr
    password: SecretStr
    client_id: SecretStr
    client_secret: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="UTF-8"
    )