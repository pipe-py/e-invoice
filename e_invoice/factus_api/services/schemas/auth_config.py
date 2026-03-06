"""Pydantic models that hold OAuth2 configuration and payload builders."""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from e_invoice.factus_api.services.tokens.token_store import token_manager


class OAuth2Credentials(BaseSettings):
    """Read OAuth2 credentials from environment variables."""

    user_name: SecretStr
    password: SecretStr
    client_id: SecretStr
    client_secret: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="UTF-8")

    def payload(self) -> dict:
        """Build the payload for the password grant type."""
        return {
            "grant_type": "password",
            "client_id": self.client_id.get_secret_value(),
            "client_secret": self.client_secret.get_secret_value(),
            "username": self.user_name.get_secret_value(),
            "password": self.password.get_secret_value(),
        }

    def header(self) -> dict:
        """Return a simple JSON header for authentication requests."""
        return {"Accept": "application/json"}


@staticmethod
class RefreshToken:
    """Create payloads and headers to refresh an access token."""

    def payload(self) -> dict:
        """Build the payload for the refresh token grant type."""
        return {
            "grant_type": "refresh_token",
            "client_id": OAuth2Credentials().client_id.get_secret_value(),
            "client_secret": OAuth2Credentials().client_secret.get_secret_value(),
            "refresh_token": token_manager._tokens["refresh_token"],
        }

    def header(self, token: str) -> dict:
        """Return a header that includes the bearer token."""
        return {"Authorization": f"Bearer {token}", "Accept": "application/json"}
