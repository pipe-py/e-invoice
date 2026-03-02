from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class OAuth2Credentials(BaseSettings):
    user_name: SecretStr
    password: SecretStr
    client_id: SecretStr
    client_secret: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="UTF-8")

    def payload(self):
        return {
            "grant_type": "password",
            "client_id": self.client_id.get_secret_value(),
            "client_secret": self.client_secret.get_secret_value(),
            "username": self.user_name.get_secret_value(),
            "password": self.password.get_secret_value(),
        }

    def header(self):
        return {"Accept": "application/json"}
